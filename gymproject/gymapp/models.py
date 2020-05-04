from django.db import models

# Create your models here.
class Workout(models.Model):
    title = models.CharField(max_length=80, nullable=False, unique=True)
    split = models.CharField(max_length=80, nullable=False)
    date = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    duration = models.IntegerField(nullable=False)