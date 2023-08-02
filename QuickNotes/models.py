from django.db import models

# Create your models here.

class Note(models.Model):
    body = models.TextField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)   # everytime note is created or updated or saved it will update the timestamp
    created = models.DateTimeField(auto_now_add=True) # only take a timestamp on creation of a note and not when we sve it or update it

    # representation
    def __str__(self):
        return self.body[0:50]