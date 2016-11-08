from django.db import models


class WorkoutProgram(models.Model):
    pass


class WorkoutDay(models.Model):
    day_name = models.CharField(max_length=20)
    workout_program = models.ForeignKey(WorkoutProgram, on_delete=models.CASCADE)


class Exercise(models.Model):
    workout_day = models.ForeignKey(WorkoutProgram, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField
    url = models.URLField


class WorkoutProgramTemplate(WorkoutProgram):
    pass


class WorkoutDayTemplate(WorkoutDay):
    pass
