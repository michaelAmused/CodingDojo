from django.shortcuts import render, redirect
from django.contrib import messages

from. models import Book, Review, Author, User
# Create your views here.
def index(request):
    if 'user' not in request.session:
        return redirect('log_reg:index')
    else:
        context = {
            'reviews': Review.objects.all().order_by('-created_at')[:3],
            'books': Book.objects.all().order_by('title')
        }
        return render(request, 'books/index.html', context)

def add_book(request):
    if 'user' not in request.session:
        return redirect('log_reg:index')
    else:
        context = {
            'authors': Author.objects.all().order_by('name')
        }
        return render(request, 'books/add.html', context)

def create(request):
    if 'user' not in request.session or request.method != 'POST':
        return redirect('log_reg:index')
    else:
        user_id = request.session['id']
        response = Book.objects.validate(request.POST, user_id)
        if response[0] == False:
            for message in response[1]:
                messages.error(request, message)
            return redirect('books:add_book')
        else:
            book_id = response[1].id
            return redirect('books:show_book', id=book_id)

def show_book(request, id):
    if 'user' not in request.session:
        return redirect('log_reg:index')
    else:
        users = User.objects.all()
        try:
            book = Book.objects.get(id=id)
            context = {
                'book': book,
                'reviews': Review.objects.filter(book=book).order_by('-created_at')
            }
            return render(request, 'books/book.html', context)
        except:
            return redirect('books:index')

def add_review(request, id):
    if 'user' not in request.session:
        return redirect('log_reg:index')
    else:
        response = Book.objects.add_review(request.POST, id, request.session['id'])
        if response[0] == False:
            for message in response[1]:
                messages.error(request, message)
        else:
            for message in response[1]:
                messages.success(request, message)
        return redirect('books:show_book', id=id)

def destroy_review(request, id, review_id):
    Review.objects.get(id=review_id).delete()
    return redirect('books:show_book', id=id)
