from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from datetime import datetime
from . import app

todo_list = [{"task": "Sample To Do", "done": False}]

@app.route("/")
def index():
    return render_template("index.html", todo_list=todo_list)

@app.route("/add", methods = ["POST"] )
def add():
    todo = request.form['todo']
    todo_list.append( {"task": todo, "done": False} )
    return redirect( url_for("index") )

@app.route("/delete/<int:index>")
def delete(index):
    del todo_list[index]
    return redirect( url_for("index") )