from flask import Flask, render_template, redirect, url_for, abort

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")