from flask import Blueprint, render_template, redirect, request, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

from app import mongo

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        try:
            username = request.form.get("username")
            password = request.form.get("password")

            if not username or not password:
                flash("Username and password are required.", "danger")
                return render_template("register.html")

            # to avoide duplicate username
            existing_user = mongo.db.users.find_one({"username": username})
            if existing_user:
                flash("Username already exists. Please choose another one.", "warning")
                return render_template("register.html")

            new_user = {
                "username": username,
                "password": generate_password_hash(password),
            }
            mongo.db.users.insert_one(new_user)
            flash("Registration successful. Please login.", "success")
            return redirect(url_for("auth.login"))
        except Exception as e:
            print(f"Error during registration: {e}")
            flash("Unexpected error during registration. Please try again.", "danger")

    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        try:
            username = request.form.get("username")
            password = request.form.get("password")

            user = mongo.db.users.find_one({"username": username})

            if user and check_password_hash(user["password"], password):
                session["user_id"] = str(user["_id"])
                flash("Login successful.", "success")
                return redirect(url_for("tasks.view_tasks"))

            flash("Invalid username or password.", "danger")
        except Exception as e:
            print(f"Error during login: {e}")
            flash("Unexpected error during login. Please try again.", "danger")

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.pop("user_id", None)
    flash("Logged out successfully.", "info")
    return redirect(url_for("auth.login"))
