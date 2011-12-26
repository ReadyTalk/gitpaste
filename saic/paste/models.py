from django.db import models
from django.contrib.auth.models import User

class Set(models.Model):
    owner = models.ForeignKey(User, null=True, blank=True, default=None)
    description = models.CharField(max_length=255)
    repo = models.CharField(max_length=15)

class Commit(models.Model):
    commit = models.CharField(max_length=255)
    set = models.ForeignKey(Set)
    created = models.DateTimeField(auto_now=True)

class Paste(models.Model):
    absolute_path = models.CharField(max_length=2048)
    filename = models.CharField(max_length=255)
    paste = models.TextField()
    paste_formatted = models.TextField()
    language = models.CharField(max_length=15)
    revision = models.ForeignKey(Commit) 
