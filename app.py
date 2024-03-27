from flask import Flask, render_template, g
import sqlite3

app  = Flask("Olá")

DATABASE = "banco.bd"

SECRET_KEY = "1234"

app.configure.from_objetc(__name__)

@app.route("/")

def conectar():
    return sqlite3.connect(DATABASE)

def before_request():
    g.bd = conectar()


def teardown_request(f):
    g.bd.close

def ola():
    return render_template("hello.html")   