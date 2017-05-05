from flask import Flask, render_template, redirect, request, session
import random
from datetime import datetime
#Interesting.  If you're going to import just what you need, you can also import randint from random like so:
#from random import randint

'''
Use newlines to your advantage to increase readability.  Keep things that are similar in nature together, I will fix this assignment, and leave the next one untouched in terms of newlines so you can practice it. - N.T.
'''

app=Flask(__name__)
app.secret_key = "getGold"

@app.route('/')
def index(): #Add a description here of your function. Ex: Initializes gold in session if it's not there and displays the main page.
    if 'gold' not in session:
        session['gold'] = 0
		
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money(): #Add a description here of your function.  See: Line 15.

    if request.form['building'] == 'farm':
        gold = random.randint(10,20)
        session['gold'] += gold
        memo = ("Earned {} golds from the farm! ({})".format(gold, datetime.now().strftime('%I:%M %p %d/%m/%Y').lower()), 'green')
		
    elif request.form['building'] == 'cave':
        gold = random.randint(5,10)
        session['gold'] += gold
        memo = ("Earned {} golds from the cave! ({})".format(gold, datetime.now().strftime('%I:%M %p %d/%m/%Y').lower()), 'green')
		
    elif request.form['building'] == 'house':
        gold = random.randint(2,5)
        session['gold'] += gold
        memo = ("Earned {} golds from the house! ({})".format(gold, datetime.now().strftime('%I:%M %p %d/%m/%Y').lower()), 'green')
		
    elif request.form['building'] == 'casino':
        toss = random.randint(0,1)
		
        if toss == 0: #No point in toss == 0...0 is falsey, so you can just say, if not toss:
            gold = random.randint(0,50)
            session['gold'] -= gold
            memo = ("lost {} golds gambling in the casino...too bad, so sad. ({})".format(gold, datetime.now().strftime('%I:%M %p %d/%m/%Y').lower()), 'red')
        else:
            gold = random.randint(0,50)
            session['gold'] += gold
            memo = ("Congratulations, you won {} golds at the casino....good going! ({})".format(gold, datetime.now().strftime('%I:%M %p %d/%m/%Y').lower()), 'green')

    try: #Interesting, I think that this belongs up there in index() since you're initializing the variables you need anyway; however, this does work okay.
        session['activity'].append(memo)
    except:
        session['activity'] = []
        session['activity'].append(memo)
	
    
    session['displayActivity'] = list(session['activity']) #Cast type not necessary, session['activity'] is already a list.
    session['displayActivity'].reverse() #Good.

    return redirect('/')

#No reset function?	

app.run(debug=True)
