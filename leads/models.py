# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from datetime import datetime


class LeadsList(models.Model):
    leads_id = models.PositiveIntegerField(null =True)
    leads_name = models.CharField(max_length=50, blank=True)
    leads_description = models.CharField(max_length=50, blank=True)

 
    def __str__(self):
        return (self.leads_name)



    


