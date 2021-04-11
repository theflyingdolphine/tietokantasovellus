from app import app
from flask import render_template, request, redirect
import users, games, reviews, statistics, re


@app.route("/")
def index():
    return render_template("index.html", reviews=reviews.findall(), statistics=statistics.showall())

@app.route("/login", methods=["get","post"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Wrong username or password")

@app.route("/signup", methods=["get","post"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    if request.method == "POST":
        username = request.form["username"]
        if len(username) < 4 or len(username) > 25:
            return render_template("error.html", message="Number of characters in the username must be within the range: 4 - 25")
        password = request.form["password"]
        password2 = request.form["password2"]
        if password == "":
            return render_template("error.html", message="The password cant be empty")
        if password != password2:
            return render_template("error.html", message="The passwords dont equal")
        role = request.form["role"]
        if users.signup(username,password,role):
            return redirect("/")
        else:
            return render_template("error.html",message="Please try again!")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/game1")
def order():
    return render_template("game1.html")

@app.route("/result", methods=["POST"])
def result():
    users.check_csrf()
    choice1 = request.form["choice1"]
    choice2 = request.form["choice2"]
    choice3 = request.form["choice3"]
    score = games.result(choice1, choice2, choice3, users.user_id())
    values = statistics.result(score)
    return render_template("result.html", choice1=choice1, choice2=choice2, choice3=choice3, score=score, values=values)

@app.route("/game2")
def order2():
    return render_template("game2.html")

@app.route("/result2", methods=["POST"])
def result2():
    users.check_csrf()
    choice1 = request.form["choice1"]
    choice2 = request.form["choice2"]
    choice3 = request.form["choice3"]
    score = games.result2(choice1, choice2, choice3)
    value =  statistics.result2(score)
    return render_template("result.html", choice1=choice1, choice2=choice2, choice3=choice3, score=score, value=value)


@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/send", methods=["POST"])
def send():
    users.check_csrf()
    content = request.form["content"]
    if reviews.send(content):
        return redirect("/")

@app.route("/newgame")
def newgame():
    return render_template("newgame.html")

@app.route("/add", methods=["POST"])
def add():
    users.check_csrf()
    question = request.form["question"]
    try:
        answer = int(request.form["answer"])
    except ValueError:
        return render_template("error.html",message="The answer must be an integer!")
    if question == "" or answer == "":
        return render_template("error.html",message="Fill in all forms!")
    if games.add(question, answer,users.user_id()):
        return redirect("/")

@app.route("/delete")
def delete():
    return render_template("delete.html")

@app.route("/remove", methods=["POST"])
def remove():
    users.check_csrf()
    if games.remove(users.user_id):
        return redirect("/")
    return render_template("error.html",message="Please try again!")

@app.route("/game3")
def game3():
    i = 0
    id = 0
    id = games.game3(i, id)
    i = 1
    question = games.game3(i, id)
    id = str(id)
    id = int(id[2:len(id)-3])
    question = str(question)
    question = question[2:len(question)-3]
    answer = 0
    correct = 0 
    return render_template("game3.html",question=question, id=id)

@app.route("/result3", methods=["POST"])
def result3():
    users.check_csrf()
    question = request.form["question"]
    id = request.form["id"]
    try:
        answer = int(request.form["answer"])
    except ValueError:
        return render_template("error.html",message="The answer must be an integer!")

    answer = int(answer)
    correct = games.result3(id)
    if answer == correct:
        statistics.result3() 
    return render_template("result3.html", myanswer=answer, correct=correct, question=question)
