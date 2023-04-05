from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("BT-Intro.html")

# @views.route('/EnterBday')
# def enterBDay():
#     return render_template("BT-EnterBDay.html")

# @views.route('/SignIn')
# def enterBDay():
#     return render_template("BT-SignIn.html")

# @views.route('/ViewBdays')
# def enterBDay():
#     return render_template("BT-ViewBDay.html")