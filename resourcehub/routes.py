from flask import render_template, flash, url_for, request, redirect
from resourcehub import app, db
# from resourcehub.models import 


@app.route("/")
def home():
    return render_template("index.html")