from flask import render_template, flash, url_for, request, redirect
from resourcehub import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from resourcehub.models import User, Resource, Comment, Subject, EducationLevel


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user: 
            if check_password_hash(user.password, password):
                flash("Logged in successfully", category="success")
            else: 
                flash("Incorrect password, try again.", category="error")
        else:
            flash("Email does not exist.", category="error")


    return render_template("login.html")


@app.route("/logout")
def logout():
    return "<p>Logout</p>"


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
            return redirect(url_for("login"))

    return render_template("signup.html")