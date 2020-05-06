from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Workout(models.Model):
    title = models.CharField(max_length=80, null=False, blank=False)
    split = models.CharField(max_length=80, null=False, blank=False)
    date = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    duration = models.IntegerField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Exercise(models.Model):
    title = models.CharField(max_length=80,null=False, blank=False, unique=True)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)