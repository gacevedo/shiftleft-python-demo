from flask import Blueprint, request, jsonify, session, redirect
from . import query_db
import bcrypt
import os

bp = Blueprint("auth", __name__)

@bp.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username is None or password is None:
        return jsonify({"error": "username and password parameter have to be provided"}), 400

    # vulnerability: SQL Injection
    # Fix: Use parameterized queries or prepared statements
    query = "SELECT id, username, access_level FROM user WHERE username = ? AND password = ?"
    result = query_db(query, (username, password), True)
    if result is None:
        return jsonify({"bad_login": True}), 400
    
    # vulnerability: Password Encryption Without Salt
    # Fix: Always use a unique salt for each user's password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    session["user_info"] = (result[0], result[1], result[2])
    return jsonify({"success": True})

@bp.route("/login_and_redirect")
def login_and_redirect():
    username = request.args.get("username")
    password = request.args.get("password")
    url = request.args.get("url")
    if username is None or password is None or url is None:
        return jsonify({"error": "username, password, and url parameters have to be provided"}), 400

    # vulnerability: SQL Injection
    # Fix: Use parameterized queries or prepared statements
    query = "SELECT id, username, access_level FROM user WHERE username = ? AND password = ?"
    result = query_db(query, (username, password), True)
    if result is None:
        # vulnerability: Open Redirect
        # Fix: Validate and sanitize the URL before using it in a redirect
        return redirect(url)
    session["user_info"] = (result[0], result[1], result[2])
    return jsonify({"success": True})



