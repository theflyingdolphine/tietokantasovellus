from db import db
from flask import abort, request, session
from werkzeug.security import check_password_hash, generate_password_hash
import os

def login(username,password):
    sql = "SELECT password, id, role FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if user == None:
        return False
    else:
        if check_password_hash(user[0],password):
            session["user_id"] = user[1]
            session["username"] = username
            session["role"] = user[2]
            session["csrf_token"] = os.urandom(16).hex()
            return True
        else:
            return False

def logout():
    del session["user_id"]
    del session["username"]
    del session["role"]

def signup(username,password,role):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username,password,role) VALUES (:username,:password,:role)"
        db.session.execute(sql, {"username":username,"password":hash_value,"role":role})
        db.session.commit()
    except:
        return False
    value1 = 0
    value2 = 0
    value3 = 0
    try:
        sql2 = "INSERT INTO statistics (username,game1,game2,other) VALUES (:username,:game1,:game2,:other)"
        db.session.execute(sql2, {"username":username,"game1":value1,"game2":value2,"other":value3})
        db.session.commit()
    except:
        return False
    return login(username,password)

def user_id():
    return session.get("user_id",0)

def admin(role):
    if role == session.get("role",0):
        return True

def name():
    name = session.get("username")
    return name

def check_csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
