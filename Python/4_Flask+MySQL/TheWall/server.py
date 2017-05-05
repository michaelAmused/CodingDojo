from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = 'ghjkllkjhkjh'

mysql = MySQLConnector(app, 'thewalldb')
bcrypt = Bcrypt(app)

email_regex = re.compile(r"[A-Za-z0-9!#$%&'*+-/=?^_`{|}~;]+@[A-Za-z0-9]+.[a-zA-Z]+")

#Main#

@app.route('/')
def index():

    if 'user' not in session:
        return render_template('login.html')

    else:
        query = 'SELECT messages.id AS id, messages.message AS message, DATE_FORMAT(messages.created_at, "%M %D %Y") AS created_at, CONCAT(users.first_name, " ", users.last_name) AS user, users.id AS user_id, TIME_TO_SEC(TIMEDIFF(CURTIME(), TIME(messages.created_at))) AS time_diff FROM messages LEFT JOIN users ON messages.user_id=users.id ORDER BY messages.created_at DESC'
        messages = mysql.query_db(query)

        query = 'SELECT comments.message_id AS id, comments.comment, DATE_FORMAT(comments.created_at, "%M %D %Y") AS created_at, CONCAT(users.first_name, " ", users.last_name) AS user FROM comments LEFT JOIN users ON comments.user_id=users.id ORDER BY comments.created_at ASC'
        comments= mysql.query_db(query)

        return render_template('index.html', messages=messages, comments=comments)

#Messages#

@app.route('/messages', methods=['POST'])
def new_message():

    data = {
        'uder_id': session['user']['id'],
        'message': request.form['message']
    }

    if len(data['message']) <= 1:
        flash('Message must be longer than 1 character.')
    else:
        query = 'INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())'

        mysql.query_db(query, data)

    return redirect('/')

@app.route('/messages/<id>/delete')
def delete_message():
    data = { 'id': id }

    messages_query = 'DELETE FROM messages WHERE id=:id'
    comments_query = 'DELETE FROM comments WHERE message_id=:id'

    mysql.query_db(comments_query, data)
    mysql.query_db(messages_query, data)

    return redirect('/')

#Comments#
@app.route('/comments', methods=['POST'])
def new_comment():

    data = {

        'user_id': session['user']['id'],
        'message_id': int(request.form['message_id']),
        'comment': request.form['comment']

    }

    query = 'INSERT INTO comments (message_id, user_id, comment, created_at, updated_at) VALUES (:message_id, :user_id, :comment, NOW(), NOW())'
    mysql.query_db(query, data)

    return redirect('/')

#Login, Registration#
@app.route('/login', methods=['POST'])
def login():
    data = {
        'email': request.form['email'],
        'password': request.form['password']
    }

    query = 'SELECT * FROM users WHERE email LIKE :email'
    user = mysql.query_db(query, data)

    if not user or len(data['password']) < 8 or not bcrypt.check_password_hash(user[0]['password'], data['password']):
        flash('User/Password combination not found')
    else:
        session['user'] = {
            'id': user[0]['id'],
            'first_name': user[0]['first_name'],
            'last_name': user[0]['last_name'],
            'email': user[0]['email']
        }

    return redirect('/')

@app.route('/register')
def show_form():

    if 'user' in session:
        return redirect('/')
    else:
        return render_template('register.html')

@app.route('/users', methods=['POST'])
def new_user():
    error = False

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password'],
        'confirm_password': request.form['confirm_password']
    }
    if data['first_name'] == "" or len(data['first_name']) < 2:
        flash('First name can not be blank or less than 2 characters')
        error = True
    if data['last_name'] == "" or len(data['last_name']) < 2:
        flash('Last name can not be blank or less than 2 characters')
        error = True
    query = 'SELECT * FROM users WHERE email LIKE :email'
    query_email = mysql.query_db(query, data)
    if query_email or data['email'] == "" or not re.match(email_regex, data['email']):
        flash('Please re-enter a valid email or login if you already are registered')
        error = True
    if len(data['password']) < 8 or data['password'] != data['confirm_password']:
        flash('Please make sure your password is at least 8 characters')
        error = True
    if error == True:
        return redirect('/register')
    else:
        data['pw_hash'] = bcrypt.generate_password_hash(data['password'])
        query = 'INSERT INTO users SET first_name=:first_name, last_name=:last_name, email=:email, password=:pw_hash, created_at=NOW(), updated_at=NOW()'
        mysql.query_db(query, data)
        flash('Successfully registered, please login')
        return redirect('/')


@app.route('/logout')
def logout():
    del session['user']
    return redirect('/')

app.run(debug=True)
