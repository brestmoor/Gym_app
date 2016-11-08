from django.db import models


class Login(models.Model):
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Role(models.Model):
    pass
