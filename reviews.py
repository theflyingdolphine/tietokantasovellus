from db import db
from flask import session

def findall():
    reviews = db.session.execute("SELECT * FROM reviews").fetchall()
    return reviews

def send(content):
    sql = "INSERT INTO reviews (content) VALUES (:content)"
    db.session.execute(sql, {"content":content})
    db.session.commit()
    return True
