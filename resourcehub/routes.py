import os
from flask import render_template, flash, url_for, request, redirect, send_file, session
from resourcehub import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from resourcehub.models import User, Resource, Comment, Subject, EducationLevel
from flask_login import login_user, login_required, logout_user, current_user
from datetime import datetime
from io import BytesIO



@app.route("/")
def home():
    """
    Renders homepage, detecting whether user is signed in. 
    """
    return render_template("index.html", user=current_user)


def redirect_url(default='index'):
    return request.referrer


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Checks email exists in user database and that the inputted hashed password matches the stored hashed password for the user. Logs user in or redirects with flashed messages.
    """
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user: 
            if check_password_hash(user.password, password):
                flash("Logged in successfully", category="success")
                login_user(user, remember=True)
                return redirect(url_for("profile"))
            else: 
                flash("Incorrect password, try again.", category="error")
        else:
            flash("Email does not exist.", category="error")

    return render_template("login.html", user=current_user)


@app.route("/logout")
@login_required
def logout():
    """
    Logs user out and redirects back to login page.
    """
    logout_user()
    return redirect(url_for("login"))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """
    Checks if email and username exist in the user database and that both password inputs match. If there is an issue, messages are flashed, otherwise new user is created and added to the database and the user is redirected to their profile page with their user id detected.
    """
    if request.method =="POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm-password")

        # Validity Check
        existing_email = User.query.filter_by(email=email).first()
        existing_username = User.query.filter_by(username=username).first()

        if existing_email and existing_username:
            flash("Username and email already exist.", category="error")
        elif existing_email: 
            flash("Email already exists.", category="error")
        elif existing_username: 
            flash("Username already exists.", category="error")
        elif password != confirm_password: 
            flash("Passwords don't match.", category="error")
        else:
            new_user = User(username=username, email=email, password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            return redirect(url_for("profile"))

    return render_template("signup.html", user=current_user)


@app.route('/profile')
@login_required
def profile():
    """
    User must be logged in to access this. Resources are rendered on the profile page and user id is detected.
    """
    resources = list(Resource.query.order_by(Resource.date_created).all())
    return render_template("profile.html", user=current_user, username=current_user.username, resources=resources)


@app.route('/edit_profile', methods=["GET", "POST"])
@login_required
def edit_profile():
    """
    Users must be logged in to access this. Users can edit their username, email or password. Detects whether an inputted username or email belongs to an existing user in the database and flashed messages if they do. Otherwise it updates user details and redirects to their profile.
    """
    if request.method =="POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        # Validity Check
        existing_email = User.query.filter_by(email=email).first()
        existing_username = User.query.filter_by(username=username).first()

        if existing_email and existing_username:
            flash("Username and email already exist.", category="error")
        elif existing_email: 
            flash("Email already exists.", category="error")
        elif existing_username: 
            flash("Username already exists.", category="error")
        else:
            if username:
                current_user.username = username
            if email:
                current_user.email = email
            if password:
                current_user.password = generate_password_hash(password)
            db.session.commit()
            flash("Profile successfully updated", category="success")

            return redirect(url_for("profile"))

    return render_template("edit_profile.html", user=current_user)


@app.route("/delete_profile/<int:user_id>")
@login_required
def delete_profile(user_id):
    """
    User must be logged in. Detects logged in user id and if it matches the user id of the profile to be deleted, allows user to be deleted from the database.
    """
    if current_user.id == user_id:
        user = User.query.get(user_id)

        if user:
            db.session.delete(user)
            db.session.commit()
            flash("Profile successfully deleted", category="success")
            return redirect(url_for("home"))
        else:
            flash("User not found", category="error")

        flash("Unauthorized action", category="error")
        return redirect(url_for("home"))


@app.route("/add_resource", methods=["GET", "POST"])
@login_required
def add_resource():
    """
    Must be logged in to access. Converts the selected subject name and education level name to the ids in the database. Creates secure filename by removing path for uploaded files, stores the binary data and saves it to the server. Adds resource to the database. 
    """
    # Define subjects and education_levels for form
    subjects = Subject.query.all()
    education_levels = EducationLevel.query.all()

    if request.method == "POST":
        resource_title = request.form.get("resource_title")
        resource_description = request.form.get("resource_description")
        subject_name = request.form.get("subject")
        education_level_name = request.form.get("education_level")

        # Convert subject and education level names to IDs
        subject_id = next((subject.id for subject in subjects if subject.subject_name == subject_name), None)
        education_level_id = next((level.id for level in education_levels if level.level == education_level_name), None)

        if "file" in request.files:
            file = request.files["file"]
            if file: 
                filename = secure_filename(file.filename)
                data = file.read()
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        
        new_resource = Resource(
            resource_title=resource_title,
            resource_description=resource_description,
            user_id=current_user.id,
            file=filename,
            data=data,
            subject_id=subject_id,
            education_level_id=education_level_id
        )
        db.session.add(new_resource)
        db.session.commit()
        flash("Resource added successfully", category="success")
        return redirect(url_for("profile"))
    
    return render_template("add_resource.html", user=current_user, username=current_user.username, subjects=subjects, education_levels=education_levels)


@app.route("/download/<resource_id>")
@login_required
def download(resource_id):
    """
    User must be logged in to access. Detects whether user is logged in. Finds resource and sends the filename and data as an attachment to the user. 
    """
    if not current_user.is_authenticated:
        flash("You need to be logged in to download resources.", category="error")
        return redirect(url_for("login"))
    
    else:
        resource = Resource.query.get_or_404(resource_id)

        if resource:
            # Retrieve only the file name
            file_name = os.path.basename(resource.file)

            # Create a BytesIO stream from the file data
            file_data = BytesIO(resource.data)

            return send_file(file_data, download_name=file_name, as_attachment=True)

        flash("Resource not found", category="error")

        return redirect(url_for("profile"))


@app.route("/view<int:resource_id>")
def view(resource_id):
    """
    Detects whether user is logged in. Allows any user to view the selected resource. If resource selected doesn't exist, user is redirected to profile if logged in or home if not logged in.
    """
    resource = Resource.query.get_or_404(resource_id)
    comments = Comment.query.filter_by(resource_id=resource_id).all()

    if resource:
        return render_template("view.html", user=current_user, resource=resource, comments=comments)
    else:
        if current_user.is_authenticated:
            flash("Resource not found", category="error")
            return redirect(url_for("profile"))
        else:
            flash("Resource not found", category="error")
            return redirect(url_for("home"))
    

@app.route("/add_comment", methods=["GET", "POST"])
@login_required
def add_comment():
    """
    User must be logged in to access. Retrieves data from form and edits existing comment in database. 
    """
    if request.method =="POST":
        comment_text = request.form.get("comment")
        resource_id = request.form.get("resource_id")

        new_comment = Comment(comment_text=comment_text, resource_id=resource_id, user_id = current_user.id)
        db.session.add(new_comment)
        db.session.commit()
        flash("Comment added successfully", category="success")

        return redirect(url_for("view", user=current_user, resource_id=resource_id))
    

@app.route("/delete_comment/<int:id>")
@login_required
def delete_comment(id):
    """
    User must be logged in to access. Detects whether user is the user who created the comment. If user is, allows deletion of comment. If not, it redirects to previous page. 
    """
    comment = Comment.query.get(id)

    if comment:
        # Check if the current user has the authorization to delete the comment
        if current_user.id == comment.user_id:
            db.session.delete(comment)
            db.session.commit()
            flash("Comment successfully deleted", category="success")
        else:
            flash("Unauthorized action", category="error")
    else:
        flash("Comment not found", category="error")

    return redirect(redirect_url())


@app.route("/edit_comment/<int:id>", methods=["GET", "POST"])
@login_required
def edit_comment(id):
    """
    User must be logged in to access. Finds comments from database. Determines whether user is the user who created the comment. If so, if there is text, edits the existing comment. If there is no comment, flashes message. 
    """
    comment = Comment.query.get(id)

    if request.method == "POST":
        new_comment_text = request.form.get("edit-comment")
        if comment:
            if current_user.id == comment.user_id:
                if new_comment_text:
                    comment.comment_text = new_comment_text
                    db.session.commit()
                    flash("Comment successfully edited", category="success")
                    print(f"Redirecting to: {redirect_url()}")
                    return redirect(url_for("profile"))
                else:
                    flash("Comment text cannot be empty", category="error")
            else:
                flash("Unauthorized action", category="error")

    return render_template("edit_comment.html", comment=comment, user=current_user)


@app.route("/subject_page/<subject_name>")
def subject_page(subject_name):
    """
    Detects subject name and renders page of resources for only that subject. Detects whether a user is logged in.
    """
    resources = Resource.query.all()
    subject_resources = []

    for resource in resources: 
        if resource.subject.subject_name.lower() == subject_name.lower():
            subject_resources.append(resource)

    return render_template("subject_page.html", user=current_user, resources=subject_resources)


@app.route('/filter/<subject_name>/<education_level>')
def filter(subject_name, education_level):
    """
    Detects subject name and education level. Renders page of resources for only that subject and education level. Detects whether a user is logged in.
    """
    resources = Resource.query.all()
    subject_resources = []

    for resource in resources: 
        if resource.subject.subject_name.lower() == subject_name.lower():
            if resource.education_level.level.lower() == education_level.lower():
                subject_resources.append(resource)
    
    return render_template('subject_page.html', user=current_user, resources=subject_resources)


@app.route("/edit_resource/<int:resource_id>", methods=["GET", "POST"])
@login_required
def edit_resource(resource_id):
    """
    User must be logged in to access. Detects with user created the resource to be edited. Users can edit title, description, subject, education level and file for existing resource. 
    """
    resource = Resource.query.get_or_404(resource_id)

    # Define subjects and education_levels for form
    subjects = Subject.query.all()
    education_levels = EducationLevel.query.all()

    if request.method == "POST":
        if current_user == resource.user:
            resource_title = request.form.get("resource_title")
            resource_description = request.form.get("resource_description")
            subject_name = request.form.get("subject")
            education_level_name = request.form.get("education_level")
            filename = None
            data = None
            # Convert subject and education level names to IDs
            subject_id = next((subject.id for subject in subjects if subject.subject_name == subject_name), None)
            education_level_id = next((level.id for level in education_levels if level.level == education_level_name), None)
            
            if subject_id is None or education_level_id is None:
                flash("Invalid subject or education level", category="error")
                return redirect(url_for("add_resource"))

            if "file" in request.files:
                file = request.files["file"]
                if file.filename: 
                    filename = secure_filename(file.filename)
                    data = file.read()
                    existing_file_path = os.path.join(app.config["UPLOAD_FOLDER"], resource.file)
                    if os.path.exists(existing_file_path):
                        os.remove(existing_file_path)

                    file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            else:
                filename = resource.file
                data = resource.data

            resource.resource_title = resource_title
            resource.resource_description = resource_description
            resource.subject_id = subject_id
            resource.education_level_id = education_level_id

            if filename is not None and data is not None:
                resource.file = filename
                resource.data = data  

            db.session.commit()
            flash("Resource updated successfully", category="success")
            return redirect(url_for("view", resource_id=resource.id))

    return render_template(
        "edit_resource.html",
        user=current_user, resource=resource, subjects=subjects, education_levels=education_levels)


@app.route("/delete_resource/<int:resource_id>")
@login_required
def delete_resource(resource_id):
    """
    User must be logged in to access. Detects whether user created resource to be edited, and if so allows deletion of resource from database. 
    """
    resource = Resource.query.get_or_404(resource_id)
    if resource: 
        if resource.user_id == current_user.id:
            db.session.delete(resource)
            db.session.commit()
            flash("Resource successfully deleted", category="success")

            return redirect(url_for("profile"))
        

@app.errorhandler(404)
def page_not_found(e):
    """
    Returns 404 page if page does not exist. Detects whether user is logged in.
    """
    return render_template('404.html', user=current_user), 404