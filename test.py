import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

db = SQL("sqlite:///finance.db")

data = db.execute("SELECT name, symbol, SUM(shares) FROM transactions WHERE user_id = user_id GROUP BY symbol ORDER by symbol")

# print (data)
# python test.py
# [{'name': 'Apple, Inc.', 'symbol': 'AAPL', 'SUM(shares)': 2}, {'name': 'Strasbaugh', 'symbol': 'STRB', 'SUM(shares)': 3}, {'name': 'Twilio, Inc.', 'symbol': 'TWLO', 'SUM(shares)': 37}]


for row in data:
        symbol = row["symbol"]
        name= row["name"]
        shares = row["SUM(shares)"]
# print (symbol)
# AAPL
# STRB
# TWLO
        db.execute("INSERT INTO portfolio (symbol, name, shares) VALUES (:symbol, :name, :shares)",
                   symbol = symbol, name = name, shares = shares,)


stocks = db.execute("SELECT * FROM portfolio")

print (stocks)

#        return render_template("index.html", stocks = stocks, cash = usd(db.execute("SELECT cash FROM users")[0]["cash"]), finaltotal = usd(float(db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])[0]["cash"]) + (db.execute("SELECT SUM(total) FROM portfolio WHERE id = :id", id = session["user_id"])[0]["SUM(total)"])))

