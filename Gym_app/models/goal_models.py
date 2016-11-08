from django.db import models


class Goal(models.Model):
    name = models.CharField(max_length=200)


class PartialGoal(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    value = models.FloatField()


class GoalRecord(models.Model):
    time = models.DateTimeField
    value = models.FloatField
