from flask import Flask, render_template, g
import sqlite3

app  = Flask("Olá")

DATABASE = "banco.bd"

SECRET_KEY = "1234"

app.config.from_object(__name__)

def conectar():
    return sqlite3.connect(DATABASE)

def before_request():
    g.bd = conectar()


def teardown_request():
    g.bd.close

@app.route("/")
def ola():
    nomeUsuario = "Danielle"
    listaUsuario = ["Lorena", "Daniel","Louise","Demethrius"]
    post = {"titulo":"Meu titulo", "texto": "Meu texto", "data_criacao":"27/03/2024"}
    return render_template("hello.html",post=post)   