import os
import random

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

# Configure application
app = Flask(__name__)

# A set of possible answers

intro = "I see you put your trust in me to make a life-changing decision for you. Alright... Maybe not life-changing, but every decision impacts your life somehow, right? So, just let me be a bit dramatic. It boosts my ego. Now, go ahead and press the 'start'-button, if you'd like, and enjoy the ride of your life!"

answer_first_part = [
    "You should totally pick option ",
    "Pick number ",
    "Well, I thought about it and to be honest, you shouldn't choose any of those. But since you must, you should go with number ",
    "Ohh yeah, that's easy, pick option ",
    "Hmmmm, that one's hard. Kiddinggg! Go with number ",
    "Hmmmm, you should totally choose option ",
    "Dear human, I would advise you to select option ",
    "I see why you couldn't decide man… Go for option "
]

answer_second_part = [
    ", for sure. I wouldn't, but you definitely should champ.",
    ". Trust me sunshine! In Noall we trust. Remember, kiddo? Uhh that sounds creepy. I apologize.",
    ", because I'm Noall and I know ALL! Get it? 'Noall' and 'know all'? Man... I'm too funny.",
    ", for the reason that my name is Noall and I know all! Get it? I know... I'm the funniest.",
    ", 100%. Believe me buttercup! This robot knows what he's talking about.",
    ", and if you don't... I'll sue your little a**!",
    ". But just for good measures... Take that with a grain of salt, buddy."
]

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():

    # "Intro" button has been clicked
    if "introBtn" in request.form:
        return render_template("name.html")

    # "Start" button has been clicked
    elif "startBtn" in request.form:
        return render_template("decisionmaker.html", step=1)

    else:
        return render_template("index.html")


@app.route("/name", methods=["GET", "POST"])
def name():

    if request.method == "POST":

        # Ensure user has submitted a name
        if not request.form.get("name"):
            return render_template("name.html", error=True)

        username = str(request.form.get("name"))
        greeting = "Hi, " + username + "! " + intro
        return render_template("intro.html", username=username, greeting=greeting)

    else:
        return render_template("name.html")


@app.route('/decisionmaker', methods=["GET", "POST"])
def decisionmaking():

    if request.method == "GET":
         return  render_template("decisionmaker.html", step=1)

    # Check if 'amount' field is present
    if "amount" in request.form:

        # Ensure user submitted a number
        if not request.form.get("amount"):
            message = "must submit an amount of options. (Come on!)"
            return  render_template("decisionmaker.html", step=1, error=True, message=message)

        amount = int(request.form.get("amount"))

        # Ensure amount >= 2 and < 5
        if amount < 2:
            message = "amount must be greater than one. (Serouisly?)"
            return  render_template("decisionmaker.html", step=1, error=True, message=message)
        elif amount > 6:
            message = "amount must be less or equal to six."
            return  render_template("decisionmaker.html", step=1, error=True, message=message)

        return render_template("decisionmaker.html", step=2, amount=amount)

    else:

        # Process the submitted options/ generate decisison (Noall's answer)

        # Determine number of amounts given by user
        max = 5
        if not request.form.get("option5"):
            max = 4
        if not request.form.get("option4"):
            max = 3
        if not request.form.get("option3"):
            max = 2

        number = random.randint(1, max)
        option = "option" + str(number)

        first_part = random.choice(answer_first_part)
        second_part =  random.choice(answer_second_part)

        answer = first_part + str(number) + ", '" + str(request.form.get(option)) + "'" + second_part

        return render_template("result.html", answer=answer)

