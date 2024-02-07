from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=2000)
    due_date = models.DateTimeField()