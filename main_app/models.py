from django.db import models
from django.contrib.auth.models import User
# from dateutil.relativedelta import relativedelta

EXERCISE_CHOICES = [
    ('Upeer Body', (
            ('bench press', 'Bench Press'),
            ('pull downs', 'Pull Downs'),
        )
    ),
    ('Lower Bodey', (
            ('squats', 'Squats'),
            ('leg curls', 'Leg Curls'),
        )
    ),
    ('Abs', (
            ('crunches', 'Crunches'),
            ('planks', 'Planks'),
        )
    ),
]

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
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateField()

    # def __str__(self):
    #     return f'{self.get_workout_display()} on {self.date}'

class Exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.CharField(
        max_length=25,
        choices=EXERCISE_CHOICES
    )
    sets = models.IntegerField()
    reps = models.IntegerField()   

