from flask import Flask, render_template, request, redirect
from db import db as handler
# FIX: Getting module errors from the above import someone pls fix thx





app = Flask(__name__)
db = handler.Database("data.db")
db.connect()

class TaskListApp:

    def __init__(self, app):
        self.app = app

    @app.route('/')
    def index():
        tasks = db.get_all_tasks()
        return render_template('index.html', tasks=tasks)

    @app.route('/add_task', methods=['POST'])
    def add_task():
        title = request.form['title']
        description = request.form['description']
        db.add_task(title, description)
        return redirect('/')

    @app.route('/update_task', methods=['POST'])
    def update_task():
        task_id = request.form['task_id']
        title = request.form['title']
        description = request.form['description']
        status = request.form['status']
        db.update_task(task_id, title, description, status)
        return redirect('/')

    @app.route('/delete_task', methods=['POST'])
    def delete_task():
        task_id = request.form['task_id']
        db.delete_task(task_id)
        return redirect('/')

