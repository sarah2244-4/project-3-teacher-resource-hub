from flask import render_template, flash, url_for, request, redirect
from resourcehub import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from resourcehub.models import User, Resource, Comment, Subject, EducationLevel
from flask_login import login_user, login_required, logout_user, current_user


@app.route("/")
def home():
    return render_template("index.html", user=current_user)


@app.route('/profile')
@login_required
def profile():
    resources = list(Resource.query.order_by(Resource.date_created).all())
    return render_template("profile.html", user=current_user, username=current_user.username, resources=resources)


@app.route("/add_resource", methods=["GET", "POST"])
def add_resource():
    if request.method == "POST":
        resource = Resource(resource_name=request.form.get("resource_title"), resource_description=request.form.get("resource_description"), url=request.form.get("url"), user_id=current_user.id)
        db.session.add(resource)
        db.session.commit()
        flash("Resource added successfully", category="success")
        return redirect(url_for("profile"))
    return render_template("add_resource.html", user=current_user, username=current_user.username)


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