# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from datetime import datetime


class CompanyList(models.Model):
    company_name = models.CharField(max_length=50, blank=True)
 
    def __str__(self):
        return (self.company_name)



    


