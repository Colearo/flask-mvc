from flask import flash, g, redirect, Flask, request
from sqlite3 import dbapi2 as sqlite3
from project import app

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

class Task(object):

    def addTask(self, task):
        db = get_db()
        db.execute('INSERT INTO Tasks (task, status) VALUES (?, ?)',
                   [request.form['task'], 0])
        db.commit()
        return True

    def delTask(self, taskId):
        db = get_db()
        db.execute('delete from Tasks where task_id = ?', taskId)
        db.commit()
        return True

    def compleTask(self, taskId):
        db = get_db()
        db.execute('update Tasks set status=1 WHERE task_id=?', taskId)
        db.commit()
        return True