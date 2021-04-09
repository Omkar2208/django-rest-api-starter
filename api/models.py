from django.db import models

class team(models.Model):
    name = models.CharField(max_length=100)
    logo = models.URLField()
    trophies = models.IntegerField()
