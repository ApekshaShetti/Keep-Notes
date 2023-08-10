from django.db import models

# Create your models here.

class User(models.Model):
    username = models.TextField(null=False,blank=False)
    email = models.TextField(null=False,blank=False,primary_key=True)
    # password = models.TextField(null=False,blank=False)
    password = models.CharField(max_length=128,null=False,blank=False, default='')


    def __str__(self):
        return self.email

class Note(models.Model):
    email = models.TextField(null=False,blank=False)
    body = models.TextField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)   # everytime note is created or updated or saved it will update the timestamp
    created = models.DateTimeField(auto_now_add=True) # only take a timestamp on creation of a note and not when we sve it or update it

    # representation
    def __str__(self):
        return self.body[0:50]