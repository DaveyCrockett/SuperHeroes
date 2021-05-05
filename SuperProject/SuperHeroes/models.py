from django.db import models

# Create your models here.


class SuperHeroes(models.Model):
    name = models.CharField(max_length=50)
    alter_ego = models.CharField(max_length=50)
    primary_power = models.CharField(max_length=50)
    secondary_power = models.CharField(max_length=50)
    catch_phrase = models.CharField(max_length=100)

    def __str__(self):
        return self.name
