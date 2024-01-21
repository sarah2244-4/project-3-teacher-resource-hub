from flask import render_template, flash, url_for, request, redirect
from resourcehub import app, db
# from resourcehub.models import User, Resource, Comment, Subject, EducationLevel


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return "<p>Login</p>"


@app.route("/logout")
def logout():
    return "<p>Logout</p>"


@app.route("/signup")
def signup():
    return "<p>Signup</p>"