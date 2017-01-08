from django.contrib.auth.models import User
from django.db import models

from Gym_app.models.person_models import Instructor
from Gym_app.models.diet_plan_models import Diet
from Gym_app.models.training_plan import TrainingPlan


class Member(User):
    registrationDate = models.DateTimeField(auto_now_add=True, blank=True)
    trainer = models.ForeignKey(Instructor, null=True, blank=True)
    plan = models.ForeignKey(TrainingPlan, null=True, blank=True)
    diet = models.ForeignKey(Diet, null=True, blank=True)

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return self.first_name, self.last_name
