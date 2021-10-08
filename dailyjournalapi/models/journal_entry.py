from django.db import models

class JournalEntry(models.Model):
    "JournalEntry Model"
    concept = models.CharField(max_length=100)
    entry = models.CharField(max_length=500)
    mood = models.ForeignKey("Mood", on_delete=models.CASCADE)
    date = models.DateField()