from django.db import models


class Values(models.Model):

  firstChar = models.CharField(max_length=40, blank=False, null=False)
  firstInt = models.IntegerField(default=1)
  secondChar = models.CharField(max_length=60, blank=True, null=True)
  secondInt = models.IntegerField(default=1)
  maxInt = models.IntegerField(default=100)
