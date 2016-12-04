from django.db import models


class CreditCard(models.Model):
    number = models.IntegerField()
    valid_through = models.DateTimeField()
    security_code = models.IntegerField()


class MembershipCard(models.Model):
    last_purchase = models.DateTimeField()
    valid_through = models.DateTimeField()
