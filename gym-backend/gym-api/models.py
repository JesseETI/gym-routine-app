from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Workout(models.Model):
    title = models.CharField(max_length=80, null=False, blank=False)
    split = models.CharField(max_length=80, null=False, blank=False)
    date = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    duration = models.CharField(max_length=80, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def author_name(self):
        return self.author.username

class Exercise(models.Model):
    title = models.CharField(max_length=80,null=False, blank=False, unique=True)
    sets = models.IntegerField(null=False, blank = False)
    reps = models.IntegerField(null=False, blank=False)
    image = models.ImageField(upload_to="", null=True, blank=True)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)