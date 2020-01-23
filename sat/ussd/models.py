from django.db import models

# Create your models here.
#users, seller,buyer, comment
class User(models.Model):
    fullname = models.CharField(max_length=25)
    Tel_No = models.CharField(max_length=20, primary_key = True)
    status = models.CharField(max_length=25)
    location = models.CharField(max_length=25)
    password = models.CharField(max_length=25)

class Buyer(models.Model):
    comment = models.CharField(max_length=140, blank=True)

class Seller(models.Model):
    comment = models.TextField(max_length=140, blank=True)
