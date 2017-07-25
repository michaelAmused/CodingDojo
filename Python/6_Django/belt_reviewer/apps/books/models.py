from __future__ import unicode_literals

from django.db import models
from ..login_registration.models import User
# Create your models here.

class BookManager(models.Manager):
    def validate(self, data, user_id):
        messages = []
        if data['title']=="":
            messages.append('Must enter title')
        elif len(data['title']) < 2:
            messages.append('Title must be more than one letter')
        if data['author'] == "" and data['author_id'] == "":
            messages.append('Must enter Author Name')
        elif data['author_id'] != "" and len(data['author']) < 2:
            messages.append('Please enter valid author name')
        elif data['author_id'] != "" and data['author'] != "":
            messages.append('Please choose author from list or enter new author')
        elif Author.objects.filter(name=data['author']):
            messages.append('The author you entered is already on the list')
        if data['review'] == "":
            messages.append('Review cannot be blank')
        elif len(data['review']) < 4:
            messages.append('Review mut be longer than three characters')

        if len(messages) > 0:
            return (False, messages)
        else:
            book = self.add_book(data, user_id)
            return (True, book)

    def get_author(self, data):
        if data['author'] != "":
            return Author.objects.create(name=data['author'])
        else:
            return Author.objects.get(id=data['author_id'])

    def add_book(self, data, user_id):
        author = self.get_author(data)
        book = Book.objects.create(title=data['title'], author=author)
        user = User.objects.get(id=user_id)
        user_review = Review.objects.create(review=data['review'], rating=data['rating'], user=user, book=book)
        return book

    def add_review(self, data, book_id, user_id):
        messages = []
        if data['review'] == "" or len(data['review']) < 4:
            messages.append('Review mut be longer than three characters')
            return (False, messages)
        else:
            user = User.objects.get(id=user_id)
            book = Book.objects.get(id=book_id)
            Review.objects.create(review=data['review'], rating=data['rating'], user=user, book=book)
            messages.append('Thanks for review!')
            return (True, messages)



class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author)
    reviews = models.ManyToManyField(User, through="Review")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
