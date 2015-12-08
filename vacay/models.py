from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class UserVacay(models.Model):
    user = models.ForeignKey('auth.User')
    days_away = models.IntegerField(default=0)
    days_here = models.IntegerField(default=0)
    vacay_days = models.IntegerField(default=0)
    
    def __str__(self):
        return '%s: %i' %(self.user, self.vacay_days)
