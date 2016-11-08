from django.db import models


class ClassInformation(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField

class Class(models.Model):
    day = models.DateField
    start_time = models.TimeField
    end_time = models.TimeField
    class_type = models.ForeignKey(ClassInformation)
