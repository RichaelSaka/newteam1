from django.db import models

class User(models.Model):
    name = models.CharField()
    username = models.CharField()
    industry_pref = models.CharField()
    location = models.CharField()
    password = models.CharField()

class Job(models.Model):
    location = models.CharField()
    position = models.CharField()
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()
    industry = models.CharField()
    level = models.CharField()
    description = models.TextField()
