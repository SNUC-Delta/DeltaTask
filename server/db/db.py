import sqlite3

class Database:
    
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.connect()


    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.create_table()


    def disconnect(self):
        if self.connection:
            self.connection.close()
        
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
                                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                title TEXT NOT NULL,
                                description TEXT,
                                status INTEGER NOT NULL)''')
        self.connection.commit()

    def add_task(self, title, description):
        self.cursor.execute('''INSERT INTO tasks (title, description, status)
                                VALUES (?, ?, ?)''', (title, description, 0))
        self.connection.commit()

    def get_all_tasks(self):
        self.cursor.execute('''SELECT id, title, description, status FROM tasks''')
        return self.cursor.fetchall()

    def get_task(self, task_id):
        self.cursor.execute('''SELECT id, title, description, status FROM tasks WHERE id = ?''', (task_id,))
        return self.cursor.fetchone()

    def update_task(self, task_id, title, description, status):
        self.cursor.execute('''UPDATE tasks SET title = ?, description = ?, status = ? WHERE id = ?''', (title, description, status, task_id))
        self.connection.commit()

    def delete_task(self, task_id):
        self.cursor.execute('''DELETE FROM tasks WHERE id = ?''', (task_id,))
        self.connection.commit()
        