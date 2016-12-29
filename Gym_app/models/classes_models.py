from django.db import models

from Gym_app.models import Instructor
from Gym_app.models import Member


class ClassInformation(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class ClassInSchedule(models.Model):
    trainer = models.ForeignKey(Instructor)
    day = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    class_type = models.ForeignKey(ClassInformation)


class Class(models.Model):
    class_in_schedule = models.ForeignKey(ClassInSchedule, null=True, blank=True)
    date = models.DateField()

    class Meta:
        abstract = True


class GroupClass(Class):
    attendees = models.ManyToManyField(Member)


class PersonalTraining(Class):
    attendee = models.ForeignKey(Member, null=True)
