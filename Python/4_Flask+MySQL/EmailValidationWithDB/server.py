from flask import Flask, render_template, session, flash, request, redirect
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)

mysql = MySQLConnector(app, 'emaildb')
app.secret_key ='secretKey'
email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success')
def success():
    query = "SELECT * FROM email_addresses"
    addresses = mysql.query_db(query)
    return render_template('success.html', addresses=addresses)

@app.route('/entry', methods=['POST'])
def entry():
    if len(request.form['email']) < 1:
        flash("Please enter email address")
        return redirect('/')
    elif not email_regex.match(request.form['email']):
        flash("invalid email address")
        return redirect('/')
    else:
        session['email'] = request.form['email']
        query = "INSERT INTO email_addresses (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {
            'email': session['email']
        }
        email_id = mysql.query_db(query, data)

        return redirect('/success')

app.run(debug=True)
