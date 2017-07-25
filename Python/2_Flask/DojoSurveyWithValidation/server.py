from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)

app.secret_key = "thisissecret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():

    if len(request.form['name']) < 1:
        flash("Name cannot be blank, please enter a name")
        name = ""
    else:
        name = request.form['name']

    if len(request.form['comment']) > 120:
        flash("comment is {} characters long, comments are limited to 120 characters".format(len(request.form['comment'])))
        comment = ""
        for num in range(121):
            comment+=request.form['comment'][num]

        comment+="..."

    else:
        comment = request.form['comment']

    dojo = request.form['dojo']
    language = request.form['language']

    return render_template('results.html', name=name, dojo=dojo, language=language, comment=comment)


app.run(debug=True)
