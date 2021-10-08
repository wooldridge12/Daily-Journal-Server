from django.db import models 

class Mood(models.Model):
    "Mood model"
    label = models.CharField(max_length=20)