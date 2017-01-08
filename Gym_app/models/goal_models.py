from django.db import models

from Gym_app.models.member import Member


class Goal(models.Model):
    member = models.ForeignKey(Member, null=True, blank=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.member.first_name + ' ' + self.member.last_name + ', ' + self.name


class PartialGoal(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    value = models.FloatField()

    def __str__(self):
        return self.goal.name + ' ' + str(self.value)


class GoalRecord(models.Model):
    goal = models.ForeignKey(Goal, null=True, blank=True)
    date = models.DateField()
    value = models.FloatField()

    def __str__(self):
        return self.goal.name + ' ' + str(self.value) + ' ' + self.date.isoformat()
