from django.shortcuts import render, redirect
import random
from datetime import datetime

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activity' not in request.session:
        request.session['activity'] = []
    print request.session['activity']
    return render(request, 'gold/index.html')


def process_money(request, data):

    if data == 'farm':
        gold = random.randint(10,20)
        request.session['gold'] += gold
        request.session['activity'].append(("Earned {} golds from the farm! ({})".format(gold, datetime.now().strftime('%I:%M %p %d/%m/%Y').lower()), 'green'))

    elif data == 'cave':
        gold = random.randint(5,10)
        request.session['gold'] += gold
        request.session['activity'].append(("Earned {} golds from the cave! ({})".format(gold, datetime.now().strftime('%I:%M %p %d/%m/%Y').lower()), 'green'))

    elif data == 'house':
        gold = random.randint(2,5)
        request.session['gold'] += gold
        request.session['activity'].append(("Earned {} golds from the house! ({})".format(gold, datetime.now().strftime('%I:%M %p %d/%m/%Y').lower()), 'green'))

    elif data == 'casino':
        toss = random.randint(0,1)

        if not toss:
            gold = random.randint(0,50)
            request.session['gold'] -= gold
            request.session['activity'].append(("lost {} golds gambling in the casino...too bad, so sad. ({})".format(gold, datetime.now().strftime('%I:%M %p %d/%m/%Y').lower()), 'red'))
        else:
            gold = random.randint(0,50)
            request.session['gold'] += gold
            request.session['activity'].append(("Congratulations, you won {} golds at the casino....good going! ({})".format(gold, datetime.now().strftime('%I:%M %p %d/%m/%Y').lower()), 'green'))

    else:
        del request.session['gold']
        del request.session['activity']

    # request.session['activity'].append(memo)


    return redirect('/')
