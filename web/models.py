from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Token(models.Model):
    user = models.OneToOneField(User, 'cascade')
    token = models.CharField(max_length=48)

    def __unicode__(self):
        return self.token


class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField(default=0)
    user = models.ForeignKey(User, 'cascade')

    def __unicode__(self):
        return self.text


class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField(default=0)
    user = models.ForeignKey(User, 'cascade')

    def __unicode__(self):
        return self.text
