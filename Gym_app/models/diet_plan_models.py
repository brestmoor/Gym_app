from django.db import models


class DietPlan(models.Model):
    pass


class DietDay(models.Model):
    diet_plan = models.ForeignKey(DietPlan)
    day_name = models.CharField(max_length=50)


class Meal(models.Model):
    diet_day = models.ForeignKey(DietDay)
    name = models.TextField(max_length=100)


class DietPlanTemplate(DietPlan):
    pass


class DietDayTemplate(DietDay):
    pass
