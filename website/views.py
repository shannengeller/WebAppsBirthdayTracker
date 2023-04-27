from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("BT-Intro.html")

@views.route('/BT-Intro.html')
def intro():
    return render_template("BT-Intro.html")

@views.route('/BT-EnterBDay.html')
def enterBDay():
    return render_template("BT-EnterBDay.html")

@views.route('/BT-SignIn.html')
def signIn():
    return render_template("BT-SignIn.html")

@views.route('/BT-ViewBDay.html')
def viewBDay():
    return render_template("BT-ViewBDay.html")

@views.route('/BT-CreateAccount.html')
def createaccount():
    return render_template("BT-CreateAccount.html")
