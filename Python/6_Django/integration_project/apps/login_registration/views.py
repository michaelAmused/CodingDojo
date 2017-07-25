from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'login_registration/index.html')

def register(request):
    if request.method == "POST":
        result = User.objects.register(first_name=request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = request.POST['password'], confirm = request.POST['confirm'])
        if result[0]:
            request.session['user'] = result[1].first_name
            request.session['bool'] = False
            return redirect('courses:index')
        else:
            for error in result[1]:
                messages.add_message(request, messages.INFO, result[1][error])
            return redirect('log_reg:index')
    else:
        messages.add_message(request, messages.INFO, 'Please Try Again')
        return redirect('log_reg:index')

def login(request):
    if request.method == "POST":
        result = User.objects.login(email = request.POST['email'], password = request.POST['password'])
        if result[0]:
            request.session['user'] = result[1].first_name
            request.session['bool'] = True
            return redirect('courses:index')
        else:
            for error in result[1]:
                messages.add_message(request, messages.INFO, result[1][error])
            return redirect('log_reg:index')
    else:
        messages.add_message(request, messages.INFO, 'Please Try Again')
        return redirect('log_reg:index')

# def success(request):
#     return render(request, 'courses/index.html')
