from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Email

# Create your views here.


def index(request):
    return render(request, 'email_valid/index.html')

def create(request):
    data = request.POST['email']
    valid, response = Email.objects.register(data)

    if valid:
        print response
        request.session['email']= response.email
        return redirect('/emails')
    else:
        messages.error(request, response)
        return redirect( '/')

def emails(request):
    context = {
    		"emails": Email.objects.all()
    	}
    return render(request, 'email_valid/emails.html', context)
