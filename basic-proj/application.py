from flask import Flask, render_template

app = Flask(__name__)

# if request is for /
#     then send back index.html
# else if request is for /zuck
#     then send zuck.html
# else if request is for /login
#     then show user login.html

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/zuck")
def zuck():
    return render_template("zuck.html")
@app.route("/login")
def login():
    return render_template("login.html")