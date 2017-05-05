from flask import Flask, request, redirect, render_template, session
app = Flask(__name__)

app.secret_key = "thisissecret"

@app.route('/')
def index():
  try:
    session['counter'] += 1
  except:
    session['counter'] = 1
  return render_template('index.html')

app.run(debug=True)
