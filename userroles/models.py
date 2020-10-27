# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from datetime import datetime


class UserRoles(models.Model):
    role_id = models.PositiveIntegerField(null =True)
    role_name = models.CharField(max_length=50, blank=True)
    role_description = models.CharField(max_length=50, blank=True)
    module_one = models.BooleanField(max_length=50, blank=True)
    module_two = models.BooleanField(max_length=1, blank=True)
    module_three = models.BooleanField(max_length=15, blank=True)
    module_four = models.BooleanField(max_length=15, blank=True)
    module_five = models.BooleanField(max_length=200, blank=True)
    modulename = models.CharField(max_length=100, blank=True)
 
    def __str__(self):
        return (self.role_name)



    


