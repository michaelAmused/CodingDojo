from __future__ import unicode_literals
import bcrypt, re
from django.contrib import messages
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
# Create your models here.
class userManager(models.Manager):
    def register(self, **kwargs):
        if kwargs is not None:
            errors = {}
            if len(kwargs['first_name']) < 2:
                errors['first_name'] = "First Name must be at least 2 characters"
            if len(kwargs['last_name']) < 2:
                errors['last_name'] = "Last Name must be at least 2 characters"
            if len(kwargs['email']) == 0:
                errors['email'] = "Email is required"
            elif not EMAIL_REGEX.match(kwargs['email']):
                errors['email'] = "Please enter a valid email"
            if len(kwargs['password']) < 8:
                errors['password'] = "Password must be at least 8 characters"
            if kwargs['password'] != kwargs['confirm']:
                errors['confirm'] = "Passwords must match"
            if len(errors) is not 0:
                return (False, errors)
            else:
                hashed = bcrypt.hashpw(kwargs['password'].encode('utf-8'), bcrypt.gensalt())
                user = User.objects.create(first_name=kwargs['first_name'], last_name=kwargs['last_name'], email=kwargs['email'], password=hashed)
                user.save()
                return (True, user)
        else:
            messages.add_message(request, messages.INFO, "Please Try Registration Again")
            return

    def login(self, **kwargs):
        if kwargs is not None:
            errors = {}
            if len(kwargs['password']) == 0:
                errors['password'] = "Please Enter a Password"
            if len(kwargs['email']) == 0:
                errors['email'] = "Please Enter a Valid Email"
            if len(errors) != 0:
                return (False, errors)
            else:
                user = User.objects.filter(email=kwargs['email'])
                if not user:
                    errors['user'] = "Email/Password Combination Not Found"
                    return (False, errors)
                else:
                    if bcrypt.checkpw(kwargs['password'].encode('utf-8'), user[0].password.encode('utf-8')):
                        return (True, user[0])
                    else:
                        errors['user'] = "Email/Password Combination Not Found"
                        return (False, errors)


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = userManager()
