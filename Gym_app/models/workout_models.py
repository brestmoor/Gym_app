from django.core.validators import validate_comma_separated_integer_list
from django.db import models

from Gym_app.models.training_plan import TrainingPlan


class Exercise(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class ExerciseInPlan(models.Model):
    plan = models.ForeignKey(TrainingPlan)
    exercise = models.ForeignKey(Exercise)
    day = models.CharField(max_length=200)
    order = models.IntegerField()
    repetitions = models.CharField(max_length=50, validators=[validate_comma_separated_integer_list])

    def __str__(self):
        return self.exercise.name + " in " + self.plan.description + " " + str(self.order)