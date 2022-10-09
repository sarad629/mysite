from flask import Flask, render_template
from flask import redirect, url_for, abort

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/narra")
def narra():
    return render_template("narra.html")

@app.route("/nipmuc")
def nipmuc():
    return render_template("nipmuc.html")

@app.route("/credit")
def credit():
    return render_template("credit.html")