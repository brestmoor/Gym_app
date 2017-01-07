from django.contrib.auth.models import User


class Instructor(User):
    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return self.first_name, self.last_name


class Manager(User):
    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return self.first_name, self.last_name
