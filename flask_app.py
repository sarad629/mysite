from flask import Flask, render_template
from flask import redirect, url_for, abort

app = Flask(__name__, static_url_path='/static')

@app.route('/',methods=['GET','POST'])
def home():
 return render_template('home.html')

@app.route("/narra")
def narra():
    return render_template("narra.html")

@app.route("/nipmuc")
def nipmuc():
    return render_template("nipmuc.html")

@app.route("/credit")
def credit():
    return render_template("credit.html")

if __name__ == '__main__':
 app.run(port=5000,debug=True)

