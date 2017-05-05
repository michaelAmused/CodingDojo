from __future__ import unicode_literals

from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class EmailManager(models.Manager):
    def register(self, data):
        if not EMAIL_REGEX.match(data):
            error = "Please enter a valid email"
            return (False, error)
        else:
            new_email = Email.objects.create(email=data)
            return (True, new_email)

class Email(models.Model):
    email = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = EmailManager()
