import sqlite3
from flask import Flask, render_template, url_for, request, flash, redirect
from flask_cors import CORS
from werkzeug.exceptions import abort

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_student(student_id):
    conn = get_db_connection()
    student = conn.execute('SELECT * FROM students WHERE Id = ?',
                        (student_id,)).fetchone()
    conn.close()
    if student_id is None:
        abort(404)
    return student

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MYSECRETKEYTHATISSECURE'
CORS(app)

@app.route('/hello')
def say_hello_world():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close
    #return render_template('index.html', students=students)
    return{'result': render_template('index.html', students=students)}

@app.route('/')
def index():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close
    return render_template('index.html', students=students)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        Student = request.form['Student']
        Id = request.form['Id']
        Marks = request.form['Marks']

        if not Student:
            flash('Name is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO students (Student, Id, Marks) VALUES (?, ?, ?)',
                         (Student, Id, Marks))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    student = get_student(id)

    if request.method == 'POST':
        Student = request.form['Student']
        Marks = request.form['Marks']

        if not Student:
            flash('Name is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE students SET Student = ?, Marks = ?'
                         ' WHERE Id = ?',
                         (Student, Marks, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', student=student)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    student = get_student(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM students WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(student['Student']))
    return redirect(url_for('index'))