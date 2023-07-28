from flask import Flask,request,render_template

app=Flask(__name__)
@app.route("/")
def index():
    return render_template("home.html")

@app.route("/order")
def order():
    return render_template("order.html")

@app.route("/check_order")
def check():
    return render_template("check.html")

@app.route("/log_in")
def log_in():
    return render_template("login.html")