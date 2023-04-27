from flask import Blueprint, render_template, request, flash, redirect, url_for
# from .models import User
# from werkzeug.security import generate_password_hash, check_password_hash
# from . import db   ##means from __init__.py import db
# from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Login</p>"


@auth.route('/logout')
def logout():
    return "<p>logout</p>"


@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>"