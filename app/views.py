from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from datetime import datetime
from . import app

todo_list = [{"task": "Sample To Do", "done": True}]

@app.route("/")
def index():
    return render_template("index.html", todo_list=todo_list)

@app.route("/add", methods = ["POST"] )
def add():
    task = request.form['task']
    todo_list.append( {"task": task, "done": False} )
    return redirect( url_for("index") )

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    task = todo_list[index]
    if request.method == "POST":
        task["task"] = request.form["task"]
        return redirect( url_for("index") )
    else:
        return render_template( "edit.html", task=task, index=index )
    
@app.route("/done/<int:index>")
def done(index):
    task = todo_list[index]
    task['done'] = not task['done']
    return redirect( url_for("index") )


@app.route("/delete/<int:index>")
def delete(index):
    del todo_list[index]
    return redirect( url_for("index") )