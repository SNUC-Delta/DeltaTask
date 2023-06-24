from flask import Flask, render_template, request, redirect
from server.db import db as handler

from tasklist import TaskListApp

# FIX: Getting module errors from the above import someone pls fix thx


app = Flask(__name__)


@app.route('/')
def index():
    tasks = tasklist.index()
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add_task():
    form = request.form
    tasklist.add_task(form)
    return redirect('/')


@app.route('/update', methods=['POST'])
def update_task():
    form = request.form
    tasklist.update_task(form)
    return redirect('/')


@app.route('/delete', methods=['POST'])
def delete_task():
    form = request.form
    tasklist.delete_task(form)
    return redirect('/')


if __name__ == '__main__':
    tasklist = TaskListApp()
    app.run(debug=True)
