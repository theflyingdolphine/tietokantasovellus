from db import db
from flask import session
import re, users
from random import randint

def result(choice1, choice2, choice3, user_id):
    score = 0
    value1 = "SELECT content FROM game1 WHERE id=1"
    correct1 = db.session.execute(value1, {"id":choice1}).fetchone()
    correct1 = re.findall(r'\d+', str(correct1))
    choice1 = re.findall(r'\d+', str(choice1))
    c1 = list(map(int, correct1))
    v1 = list(map(int, choice1))
    if c1 == v1:
        score +=1
    
    value2 = "SELECT content FROM game1 WHERE id=2"
    correct2 = db.session.execute(value2, {"id":choice2}).fetchone()
    correct2 = re.findall(r'\d+', str(correct2))
    choice2 = re.findall(r'\d+', str(choice2))
    c2 = list(map(int, correct2))
    v2 = list(map(int, choice2))
    if c2 == v2:
        score +=1

    value3 = "SELECT content FROM game1 WHERE id=3"
    correct3 = db.session.execute(value3, {"id":choice3}).fetchone()
    correct3 = re.findall(r'\d+', str(correct3))
    choice3 = re.findall(r'\d+', str(choice3))
    c3 = list(map(int, correct3))
    v3 = list(map(int, choice3))
    if c3 == v3:
        score +=1

    return c1,v1

def result2(choice1, choice2, choice3):
    score = 0
    value1 = "SELECT content FROM game2 WHERE id=1"
    correct1 = db.session.execute(value1, {"id":choice1}).fetchone()
    correct1 = re.findall(r'\d+', str(correct1))
    choice1 = re.findall(r'\d+', str(choice1))
    c1 = list(map(int, correct1))
    v1 = list(map(int, choice1))
    if c1 == v1:
        score +=1
    
    value2 = "SELECT content FROM game2 WHERE id=2"
    correct2 = db.session.execute(value2, {"id":choice2}).fetchone()
    correct2 = re.findall(r'\d+', str(correct2))
    choice2 = re.findall(r'\d+', str(choice2))
    c2 = list(map(int, correct2))
    v2 = list(map(int, choice2))
    if c2 == v2:
        score +=1

    value3 = "SELECT content FROM game2 WHERE id=3"
    correct3 = db.session.execute(value3, {"id":choice3}).fetchone()
    correct3 = re.findall(r'\d+', str(correct3))
    choice3 = re.findall(r'\d+', str(choice3))
    c3 = list(map(int, correct3))
    v3 = list(map(int, choice3))
    if c3 == v3:
        score +=1
    return score

def add(question, answer, user_id):
    sql = "INSERT INTO game3 (creator,question,answer) VALUES (:creator,:question,:answer)"
    db.session.execute(sql, {"creator":user_id,"question":question,"answer":answer})
    db.session.commit()
    return True

def game3(i, id):
    if i == 0:
        sql = "SELECT COUNT(*) FROM game3"
        size = db.session.execute(sql).fetchone()[0]
        which = randint(0, size-1)
        question_id = ("SELECT id FROM game3 LIMIT 1 OFFSET :which")
        values = db.session.execute(question_id, {"which":which}).fetchall()
        
    else:
        id = str(id)
        id = int(id[2:len(id)-3])
        question = ("SELECT question FROM game3 WHERE id=:id")
        values = db.session.execute(question, {"id":id}).fetchone()
    return values

def result3(id):
    value = int(id)
    correct = "SELECT answer FROM game3 WHERE id=:id"
    correct = db.session.execute(correct, {"id":value}).fetchone()
    correct = str(correct)
    correct = int(correct[1:len(correct) - 2])
    return correct

def remove(user_id):
    sql = "DELETE FROM game3 WHERE creator=creator"
    db.session.execute(sql, {"creator":user_id})
    db.session.commit()
    return True
