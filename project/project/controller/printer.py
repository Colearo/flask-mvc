from project import app
from project.models import Task
from flask import render_template, request

from flask import flash, g, redirect, Flask, url_for
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

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/task',methods=['GET','POST'])
def task():
    db = get_db()
    cur = db.execute('SELECT task_id ,task, status FROM Tasks ORDER BY task_id DESC')
    tasks = cur.fetchall()
    return render_template('task.html', tasks=tasks)

@app.route('/task/add',methods=['GET','POST'])
def addTask():
    if request.method=='POST':
        # return request.form['task']
        task = Task()
        task.addTask(request.form['task'])
        return redirect(url_for('task'))
    return render_template('addTask.html')

@app.route('/task/delete/<id>',methods=['GET','POST'])
def delTask(id):
    task = Task()
    task.delTask(id)
    return redirect(url_for('task'))

@app.route('/task/complete/<id>',methods=['GET','POST'])
def compleTask(id):
    task = Task()
    task.compleTask(id)
    return redirect(url_for('task'))


