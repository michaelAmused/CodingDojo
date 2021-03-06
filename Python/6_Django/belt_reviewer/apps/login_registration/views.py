from django.shortcuts import render, redirect
from .models import User
from ..books.models import Review, Author, Book
from django.contrib import messages

# Create your views here.
def index(request):
    if 'user' in request.session:
        return redirect('books:index')
    else:
        return render(request, 'login_registration/index.html')

def register(request):
    if request.method == "POST":
        result = User.objects.register(first_name=request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = request.POST['password'], confirm = request.POST['confirm'])
        if result[0]:
            request.session['id'] = int(result[1].id)
            request.session['user'] = result[1].first_name
            request.session['bool'] = False
            return redirect('books:index')
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
            request.session['id'] = int(result[1].id)
            request.session['user'] = result[1].first_name
            request.session['bool'] = True
            return redirect('books:index')
        else:
            for error in result[1]:
                messages.add_message(request, messages.INFO, result[1][error])
            return redirect('log_reg:index')
    else:
        messages.add_message(request, messages.INFO, 'Please Try Again')
        return redirect('log_reg:index')

def logout(request):
    request.session.clear()
    return redirect('log_reg:index')

def user_reviews(request, id):
    if id:
        user = User.objects.get(id=id)
        context = {
            'user': {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
            },
            'user_reviews': Review.objects.filter(user=user).order_by('book__title'),
            'count_reviews': Review.objects.filter(user=user).count()
        }
        return render(request, 'login_registration/user_reviews.html', context)
    else:
        return redirect('books:index')
