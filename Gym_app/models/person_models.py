from django.contrib.auth.models import User
from django.db import models


class Member(User):
    registrationDate = models.DateTimeField(auto_now_add=True, blank=True)

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return self.last_name


class Instructor(User):
    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return self.last_name


class Manager(User):
    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return self.last_name
