from flask import render_template, flash, url_for, request, redirect
from resourcehub import app, db
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
    return render_template("signup.html")