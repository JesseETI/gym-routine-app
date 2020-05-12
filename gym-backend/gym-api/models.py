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

    def exercises_list(self):
        exercise_queryset = Exercise.objects.filter(workout = self)
        exercise_list = []
        for exercise in exercise_queryset:
            exercise_list.append(exercise)
        return exercise_list

class Exercise(models.Model):
    title = models.CharField(max_length=80,null=False, blank=False, unique=True)
    image = models.ImageField(upload_to="", null=True, blank=True)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)