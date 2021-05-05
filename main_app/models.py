from django.db import models
from django.contrib.auth.models import User
# from dateutil.relativedelta import relativedelta

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    nickname = models.CharField(max_length=25)
    age = models.IntegerField()
    # dob = models.DateField(max_length=8)
    # height = models.IntegerField()
    # weight = models.IntegerField()
    # bmi = models.IntegerField()
    # weightgoal = models.IntegerField()

    # def __str__(self):
    #     today = date.today()
    #     delta = relativedelta(today, self.dob)
    #     return str(delta.years)

class Workout(models.Model):
    exercise = models.CharField(max_length=25)
    sets = models.IntegerField()
    reps = models.IntegerField()

workouts = [
    Workout('squats', 4, 12),
    Workout('leg curls', 4, 20),
    Workout('calf raises', 5, 50),
]
