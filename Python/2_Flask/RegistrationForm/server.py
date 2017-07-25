from flask import Flask, render_template, redirect, request, session, flash
import re
from datetime import datetime, date
#Clean imports this time, nice.

#Please fix your newlines (See the assignment prior to this: Ninja Gold). I didn't touch the newline spacing on this one. - N.T.

app = Flask(__name__)

app.secret_key = "itsAsecret"

email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
pwd_regex = re.compile(r'^(?=[^A-Z]*[A-Z])(?=[^0-9]*[0-9])[\w\d]{8,}$')
date_regex = re.compile(r'([0-1][0-9])\/([0-3][0-9])\/([1-9][0-9][0-9][0-9])')

@app.route('/')
def index(): #Need description. Especially this.../form and / do the same thing? If this was intentional, ask me about using double decorators (two routes leading to the same function).
    return redirect('/form')

@app.route('/form')
def reg(): #Need description.

    return render_template('index.html')

@app.route('/process', methods=['POST'])
def valid(): #Need description.

    if len(request.form['email']) < 1:
        flash("Email must have valid email address", 'empty')
    elif not email_regex.match(request.form['email']):
        flash("'{}' is not a valid email address".format(request.form['email']), 'invalid')

    else:
        email = request.form['email']


    if len(request.form['first_name']) < 1:
        flash("Please enter your first name", 'empty')
    elif not request.form['first_name'].isalpha():
        flash("Please enter a valid first name", 'invalid')
    else:
        first_name = request.form['first_name']

    if len(request.form['last_name']) < 1:
        flash("Please enter your last name", 'empty')
    elif not request.form['last_name'].isalpha():
        flash("Please enter a valid last name", 'invalid')
    else:
        first_name = request.form['last_name']
	#Good use of isalpha().
    password = request.form['password']
	# ^ If you're going to pull it out into a variable....Then you should probably use it consistently.
    if len(request.form['password']) < 1: # See the line above ^.
        flash("Please enter a password", 'empty')
    elif not pwd_regex.match(password):
        flash("Password must be at least 8 characters and include at least 1 uppercase and 1 number", 'invalid')
    elif password != request.form['confirm_password']:
        print password
        print request.form['confirm_password']
        flash("Passwords do not match", 'invalid')

    birthdateValid = date_regex.match(request.form['birth_date'])
    today = date.today()

    if len(request.form['birth_date']) < 1:
        flash("Please enter a valid date", 'empty')
    else:
        if not birthdateValid:
            flash("Please enter date in the format: MM/DD/YYYY", 'invalid')
        else:
            birth_date = date(int(birthdateValid.group(3)), int(birthdateValid.group(1)), int(birthdateValid.group(1)))
            if not birth_date < today:
                flash("Please enter your Birth Date and not Today's date", 'invalid')
			# ^ What if your user was 500000 years old?
    return redirect('/')

app.run(debug=True)
