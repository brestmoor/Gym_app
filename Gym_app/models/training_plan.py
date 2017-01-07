from django.contrib.auth.models import User
from django.db import models

from Gym_app.models.person_models import Instructor


class TrainingPlan(models.Model):
    trainer = models.ForeignKey(Instructor)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        if self.description is None:
            return str(self.pk)
        else:
            return self.description
