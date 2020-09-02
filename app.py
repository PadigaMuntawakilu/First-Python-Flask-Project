from flask import Flask, render_template, request, session

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("home.html")

@app.route("/urlshortner")
def urlshortner():
    return render_template("form.html")