import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
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
    user_id = session["user_id"]
    db.execute("DELETE FROM portfolio")
    data = db.execute(
        "SELECT name, symbol, SUM(shares) FROM transactions WHERE user_id = :user_id GROUP BY symbol ORDER by symbol", user_id=user_id)

    for row in data:
        symbol = row["symbol"]
        name = row["name"]
        shares = row["SUM(shares)"]
        price = lookup(symbol)["price"]
        total = price * shares
        #result = db.execute("SELECT symbol FROM transactions WHERE symbol = :symbol", symbol = row["symbol"])
        db.execute("INSERT OR REPLACE INTO portfolio (symbol, name, shares, price, total, id) VALUES (:symbol, :name, :shares, :price, :total, :id)",
                   symbol=symbol, name=name, shares=shares, price=price, total=total, id=session["user_id"])
        # if result:
        # db.execute("UPDATE portfolio SET shares= :shares, total= :total WHERE symbol= :symbol", shares = shares, total = total, symbol = symbol)
        # else:
        # db.execute("INSERT INTO portfolio (symbol, name, shares, price, total, id) VALUES (:symbol, :name, :shares, :price, :total, :id)",
        # symbol = symbol, name = name, shares = shares, price = price, total = total, id = session ["user_id"])

    stocks = db.execute("SELECT * FROM portfolio")
    for row in stocks:
        row["price"] = usd(row["price"])
        row["total"] = usd(row["total"])
    cash = float(db.execute("SELECT cash FROM users WHERE id = :user_id", user_id=user_id)[0]["cash"])
    totalsum = db.execute("SELECT SUM(total) FROM portfolio WHERE id = :user_id", user_id=user_id)
    if totalsum[0]["SUM(total)"] is not None:
        totalsum = float(totalsum[0]["SUM(total)"])
    else:
        totalsum = 0
    finaltotal = usd(cash + totalsum)
    return render_template("index.html", stocks=stocks, cash=usd(cash), finaltotal=finaltotal)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        time = datetime.now()
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
            return apology("Must provide positive integer", 403)
        if int(request.form.get("shares")) <= 0:
            return apology("Must provide positive integer", 403)

        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))
        result = lookup(symbol)
        name = result["name"]
        price = result["price"]
        symbol = result["symbol"]
        total = shares * price
        money_left = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])[0]["cash"]
        money_left = money_left - total

        if money_left < 0:
            return apology("You cannot afford the number of shares at the current price", 403)

        db.execute("INSERT INTO transactions (symbol, name, shares, price, user_id, time) VALUES (:symbol, :name, :shares, :price, :id, :time)",
                   symbol=symbol, name=name, shares=shares, price=price, id=session["user_id"], time=time)

        db.execute("UPDATE users SET cash = :money_left WHERE id = :id", id=session["user_id"], money_left=money_left)

        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():

    transactions = db.execute("SELECT * FROM transactions WHERE user_id = :user_id", user_id=session["user_id"])
    for row in transactions:
        row["price"] = usd(row["price"])
    return render_template("history.html", transactions=transactions)


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

        return render_template("quoted.html", name=result["name"], price=usd(result["price"]), symbol=result["symbol"])

    else:
        return render_template("quote.html")


# Section Walkthrough 11/19
@app.route("/register", methods=["GET", "POST"])
def register():

    # forget any user_id
    session.clear()

    if request.method == "POST":

        password = request.form.get("password")

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # check if password is at least 6 letters
        elif len(password) < 6:
            return apology("password must be at least 6 characters", 403)

        # https://stackoverflow.com/questions/17140408/if-statement-to-check-whether-a-string-has-a-capital-letter-a-lower-case-letter/17140466
        # check if there is not one capital letter
        elif not any(x.isupper() for x in password):
            return apology("password must have at least one upper case letter", 403)

        # check if there is not one number
        elif not any(x.isdigit() for x in password):
            return apology("password must have at least one number", 403)

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
            db.execute("INSERT INTO users (username, hash) VALUES (:username, :hsh)",
                       username=request.form.get("username"), hsh=hsh)
            # make session the user id of who just registered
            session["user_id"] = db.execute("SELECT id FROM users WHERE username = :username",
                                            username=request.form.get("username"))[0]["id"]
            # redirect to homepage
            return redirect("/")

    else:
        # render register page
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    stocks = db.execute("SELECT * FROM portfolio WHERE id = :id", id=session["user_id"])
    if request.method == "POST":

        symbol = request.form.get("symbol")
        # check stock is selelected
        if not symbol:
            return apology("must select stock", 403)

        # check if (somehow, once submitted) the user does not own any shares of that stock.
        match = False
        for stock in stocks:
            if symbol == stock["symbol"]:
                match = True
        if match == False:
            return apology("You do not own any shares of that stock", 403)

        shares_sold = request.form.get("shares")
        if not shares_sold.isdigit():
            return apology("Must provide positive integer", 403)
        if int(shares_sold) <= 0:
            return apology("Must provide positive integer", 403)
        shares_sold = int(shares_sold)
        current_shares = db.execute("SELECT shares FROM portfolio WHERE (symbol = :symbol AND id = :id)",
                                    symbol=symbol, id=session["user_id"])[0]["shares"]
        current_shares = int(current_shares)
        current_price = db.execute("SELECT price FROM portfolio WHERE (symbol = :symbol AND id = :id)",
                                   symbol=symbol, id=session["user_id"])[0]["price"]
        current_total = db.execute("SELECT total FROM portfolio WHERE (symbol = :symbol AND id = :id)",
                                   symbol=symbol, id=session["user_id"])[0]["total"]

        # check if you have enough shares of certain stock to sell
        if int(shares_sold) > current_shares:
            return apology("You do not own that many shares of the stock", 403)

        # get current cash
        cash = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])[0]["cash"]

        # make new cash
        new_cash = cash + (shares_sold * current_price)

        # update cash
        db.execute("UPDATE users SET cash = :new_cash WHERE id = :id", new_cash=new_cash, id=session["user_id"])

        # define new shares and new total
        #new_shares = current_shares - shares_sold
        #new_total = usd(current_total - (shares_sold * current_price))

        # update portfolio
        #db.execute("UPDATE portfolio SET (shares, total) = (:new_shares, :new_total) WHERE (symbol = :symbol AND id = :id)", new_shares = new_shares, new_total = new_total, symbol = symbol, id = session["user_id"])

        # FOR TRANSACTIONS
        symbol = request.form.get("symbol")
        name = lookup(symbol)["name"]
        shares_sold = -int(request.form.get("shares"))
        price = lookup(symbol)["price"]
        time = datetime.now()

        # insert new row in transactions for each sell
        db.execute("INSERT INTO transactions (symbol, name, shares, price, user_id, time) VALUES (:symbol, :name, :shares_sold, :price, :id, :time)",
                   symbol=symbol, name=name, shares_sold=shares_sold, price=price, id=session["user_id"], time=time)

        return redirect("/")
    else:
        return render_template("sell.html", stocks=stocks)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
