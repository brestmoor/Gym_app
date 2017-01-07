from django.db import models

from Gym_app.models.person_models import Instructor


class Diet(models.Model):
    trainer = models.ForeignKey(Instructor, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        if self.description is None:
            return str(self.pk)
        else:
            return self.description



class Meal(models.Model):
    plan = models.ForeignKey(Diet, null=True)
    name = models.TextField(max_length=100)
    quantity = models.IntegerField()
    calories = models.IntegerField()
    order = models.IntegerField()
    day = models.CharField(max_length=100)


