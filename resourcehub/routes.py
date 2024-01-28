import os
from flask import render_template, flash, url_for, request, redirect, send_file
from resourcehub import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from resourcehub.models import User, Resource, Comment, Subject, EducationLevel
from flask_login import login_user, login_required, logout_user, current_user
from datetime import datetime
from io import BytesIO


@app.route("/")
def home():
    return render_template("index.html", user=current_user)


@app.route("/login", methods=["GET", "POST"])
def login():
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
    logout_user()
    return redirect(url_for("login"))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method =="POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm-password")

        # Validity Check
        user = User.query.filter_by(email=email).first()
        if user: 
            flash("Email already exists.", category="error")
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
    # 
    resources = list(Resource.query.order_by(Resource.date_created).all())
    return render_template("profile.html", user=current_user, username=current_user.username, resources=resources)


@app.route("/add_resource", methods=["GET", "POST"])
@login_required
def add_resource():
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
        
        if subject_id is None or education_level_id is None:
            flash("Invalid subject or education level", category="error")
            return redirect(url_for("add_resource"))

        if "file" in request.files:
            file = request.files["file"]
            filename = secure_filename(file.filename)
            data = file.read()
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                
        else:
            flash("Invalid file", category="error")
            return redirect(url_for("add_resource"))
        
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
    resource = Resource.query.get_or_404(resource_id)

    if resource:
        # Retrieve only the file name
        file_name = os.path.basename(resource.file)

        # Create a BytesIO stream from the file data
        file_data = BytesIO(resource.data)

        return send_file(file_data, download_name=file_name, as_attachment=True)

    # Handle the case where the resource with the given ID is not found
    flash("Resource not found", category="error")

    return redirect(url_for("profile"))


@app.route("/view<int:resource_id>")
def view(resource_id):
    resource = Resource.query.get_or_404(resource_id)

    if resource:
        return render_template("view.html", user=current_user, resource=resource)
    else:
        flash("Resource not found", category="error")
        return redirect(url_for("profile"))