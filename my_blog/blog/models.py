from pyexpat import model
from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=90)
    descripton = models.TextField()
    education = models.TextField()
    age = models.SmallIntegerField()
    courses = models.CharField(max_length=200)
    skills = models.TimeField()
    book = models.CharField(max_length=250)
