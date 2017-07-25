from flask import Flask, request, redirect, render_template, session, flash
import random

app = Flask(__name__)

app.secret_key = "thisissecret"

@app.route('/')
def index():
    if 'rand_num' not in session:
        session['rand_num'] = random.randint(1,100)
    try:
        if session['guess'] < session['rand_num']:
            session['message'] = 'Guess is too low!'
        elif session['guess'] > session['rand_num']:
            session['message'] = 'Guess is too high!'
        elif session['guess'] == session['rand_num']:
            session['winner'] = True
    except:
        pass

    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():

    if 'user_input' in request.form:

        try:
            session['guess'] = int(request.form['guess'])

        except:
            session['guess'] = 0

    elif 'play_again' in request.form:
        session.pop('guess')
        session.pop('winner')
        session.pop('rand_num')

    if 'message' in session:
        session.pop('message')

    return redirect('/')


app.run(debug=True)
