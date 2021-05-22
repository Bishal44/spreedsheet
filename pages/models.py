from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=10000)
    response = models.CharField(max_length=500,blank=True)
    permit = models.CharField(max_length=500,blank=True)
    comments = models.CharField(max_length=500, blank=True)
