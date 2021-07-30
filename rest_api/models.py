from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=150, blank=True)


class Point(models.Model):
    points = models.CharField(max_length=300, blank=False)
    closetpointpair = models.CharField(max_length=100, blank=False)
    closetdistance = models.CharField(max_length=200, blank=False)
    createdDate = models.DateTimeField(auto_now_add=True)
   