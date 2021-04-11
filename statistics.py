from db import db
from flask import session
import re, users

def showall():
    if users.admin(2):
        statistics = db.session.execute("SELECT username,game1,game2,other FROM statistics").fetchall()
    else:
        username = users.name()
        statistics = "SELECT username,game1,game2,other FROM statistics WHERE username=:username"
        statistics = db.session.execute(statistics, {"username":username}).fetchall()
    return statistics

def result(score):
    name = users.name()
    old = "SELECT game1 FROM statistics WHERE username=:username"
    old = db.session.execute(old, {"username":name}).fetchone()
    old = re.findall(r'\d+', str(old))
    old = list(map(int, old))
    old2 = 0
    for i in range(len(old)):
        old2 +=i
    old = old2
    game1 = score
    if game1 > old:
        sql = "UPDATE statistics SET game1=:game1 WHERE username=:username"
        db.session.execute(sql, {"game1":game1,"username":name})
        db.session.commit()
    return True

def result2(score):
    name = users.name()
    old = "SELECT game2 FROM statistics WHERE username=:username"
    old = db.session.execute(old, {"username":name}).fetchone()
    old = re.findall(r'\d+', str(old))
    old = list(map(int, old))
    old2 = 0
    for i in range(len(old)):
        old2 +=i
    old = old2
    game2 = score
    if game2 > old:
        sql = "UPDATE statistics SET game2=:game2 WHERE username=:username"
        db.session.execute(sql, {"game2":game2,"username":name})
        db.session.commit()
    return name

def result3():
    name = users.name()
    update = "UPDATE statistics SET other=other+1 WHERE username=:username"
    db.session.execute(update, {"username":name})
    db.session.commit()
    return True
