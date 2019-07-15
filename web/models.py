from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField(default=0)
    user = models.ForeignKey(User, 'cascade')


class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField(default=0)
    user = models.ForeignKey(User, 'cascade')
