from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# @app.route('/results')
# def results():
#     return render_template("results.html",name=name,dojo=dojo,language=language,comment=comment)

@app.route('/users', methods=['POST'])
def create_user():
    print "Creating user"
    print request.form
    form_results = {
        'name': request.form['name'],
        'dojo': request.form['dojo'],
        'language': request.form['language'],
        'comment': request.form['message']
    }
    return render_template("result.html",results=form_results)
app.run(debug=True) # run our server
