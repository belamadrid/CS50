import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    data = db.execute("SELECT name, symbol, SUM(shares) FROM transactions WHERE user_id = :id GROUP BY symbol", id = session["user_id"])
    for row in data:
        symbol = data[row]["symbol"]
        name = data[row]["name"]
        shares = data[row]["SUM(shares)"]
        price = lookup("symbol")
        total = price * shares
        db.execute("INSERT INTO portfolio (symbol, name, shares, price, total, id) VALUES (:symbol, :name, :shares, :price, :total, :id)", symbol = symbol, name = name, shares = shares, price = price, total = total, id = session["user_id"])

    return render_template("index.html", stocks = db.execute("SELECT * FROM portfolio"), cash = db.execute("SELECT cash FROM users"), finaltotal = db.execute("SELECT SUM(total) FROM portfolio WHERE id = :id", id = session["user_id"])


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":

        # Ensure valid symbol was submitted
        if not request.form.get("symbol"):
            return apology("must provide symbol", 403)

        if (lookup(request.form.get("symbol")) == None):
            return apology("Must provide valid symbol", 403)

        # Ensure valid shares was submitted
        if not request.form.get("shares"):
            return apology("must provide shares", 403)

        # https://stackoverflow.com/questions/22025764/python-check-for-integer-input
        if not request.form.get("shares").isdigit():
            return apology("Must provide positive integer")
        if int(request.form.get("shares")) <= 0:
            return apology("Must provide positive integer")

        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))
        result = lookup(symbol)
        name = result["name"]
        price = result["price"]
        symbol = result["symbol"]
        total = shares * price
        money_left = db.execute("SELECT cash FROM users WHERE id = :id",id = session["user_id"])[0]["cash"]
        money_left = money_left - total

        if money_left < 0:
            return apology("You cannot afford the number of shares at the current price", 403)

        db.execute("INSERT INTO transactions (symbol, name, shares, price, user_id) VALUES (:symbol, :name, :shares, :price, :id)", symbol = symbol, name = name, shares = shares, price = price, id = session["user_id"])

        db.execute("UPDATE users SET cash = :money_left WHERE id = :id", id = session["user_id"], money_left = money_left)

        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("must provide symbol", 403)

        result = lookup(request.form.get("symbol"))

        if result == None:
            return apology("Invalid symbol", 403)

        return render_template("quoted.html", name = result["name"], price = usd(result["price"]), symbol = result["symbol"])

    else:
        return render_template("quote.html")


# Section Walkthrough 11/19
@app.route("/register", methods=["GET", "POST"])
def register():

    # forget any user_id
    session.clear()

    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Ensure confirmation was submitted
        elif not request.form.get("confirmation"):
            return apology("must provide password confirmation", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))
        # check that the number of rows of people who have that username is 0
        if len(rows) != 0:
            return apology("Username taken", 403)

        # check if passwords match
        if request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords do not match", 403)

        # if username is not taken and passwords match, register them
        else:
            # generate hash of password
            hsh = generate_password_hash(request.form.get("password"))
            # insert username and password hash into users table
            db.execute("INSERT INTO users (username, hash) VALUES (:username, :hsh)", username=request.form.get("username"), hsh=hsh)
            # make session the user id of who just registered
            session["user_id"] = db.execute("SELECT id FROM users WHERE username = :username", username=request.form.get("username"))[0]
            # redirect to homepage
            return redirect("/")

    else:
        # render register page
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
