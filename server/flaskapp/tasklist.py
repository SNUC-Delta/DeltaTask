from server.db import db as handler

from flask import render_template, request, redirect


class TaskListApp:
    def __init__(self):
        self.db = handler.Database("data.db")

    def index(self) -> list:
        tasks = self.db.get_all_tasks()
        return tasks

    def add_task(self, form) -> None:
        title = form['title']
        description = form['description']
        self.db.add_task(title, description)

    def update_task(self, form) -> None:
        task_id = form['task_id']
        title = form['title']
        description = form['description']
        status = form['status']
        self.db.update_task(task_id, title, description, status)

    def delete_task(self, form) -> None:
        task_id = form['task_id']
        self.db.delete_task(task_id)
