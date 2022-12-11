from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
  return render_template("index.html")


@app.route("/contatos")
def contatos():
  return render_template("contatos.html")


@app.route("/sobre")
def sobre():
  return render_template("sobre.html")


@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
  return render_template("usuarios.html", nome_usuario=nome_usuario)


