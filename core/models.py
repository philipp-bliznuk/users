# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class UserAccount(models.Model):
    SEX_CHOICES = (
        (0, 'Male'),
        (1, 'Female'),
    )

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return '{self.name} {self.surname}'.format(self=self)


class Activity(models.Model):
    user = models.ForeignKey(UserAccount, related_name='activities')
    name = models.CharField(max_length=255)
