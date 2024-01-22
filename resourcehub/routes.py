from flask import render_template, flash, url_for, request, redirect
from resourcehub import app, db
from werkzeug.security import generate_password_jash, check_password_hash
# from resourcehub.models import User, Resource, Comment, Subject, EducationLevel


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
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
        confirmPassword = request.form.get("confirm-password")

        # Validity Check
        if password != confirmPassword: 
            pass
        else:
            new_user = User(username=username, email=email, password=generate_password_hash(password, method="sha256"))
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for("home"))

    return render_template("signup.html")