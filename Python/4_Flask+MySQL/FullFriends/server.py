from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)

app.secret_key = "this is secret"
mysql = MySQLConnector(app, 'friendsdb')
email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    query = "SELECT * FROM friends "
    friends = mysql.query_db(query)
    return render_template('index.html', friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    errors = False
    if len(request.form['first_name']) < 2:
        flash('Name must be at least 2 characters')
        errors = True
    if len(request.form['last_name']) < 2:
        flash('Name must be at least 2 characters')
        errors = True
    if not email_regex.match(request.form['email']):
        flash('Invalid Email')
        errors = True
    if errors:
        return redirect('/')
    else:
        query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
        }
        user_id = mysql.query_db(query, data)
        session['user_id'] = user_id
        return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
    print "hello"
    query = "SELECT * FROM friends WHERE id = :id "
    data = {
        'id': id
    }
    friend = mysql.query_db(query, data)
    print "halfway"
    return render_template('edit.html' , friend=friend[0] )

@app.route('/friends/<id>', methods=['POST'])
def update(id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id "
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'id': id
    }
    mysql.query_db(query, data)

    return redirect('/')

@app.route('/friends/<id>/delete')
def destroy(id):
    # form a query to delete a user
    query = "DELETE FROM friends WHERE id = :id "
    data = {
        'id': id
    }

    mysql.query_db(query, data)

    return redirect('/')



app.run(debug=True)
