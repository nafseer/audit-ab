# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from django.utils import timezone

class LeadSheetsMasterNew(models.Model):
    leadsheets = models.CharField(max_length=50, null=True,blank=True)
    def __str__(self):
        return str(self.leadsheets)

class ProgramListMaster(models.Model):
    
    program_name = models.CharField(max_length=50, blank=True)
    leadsheets = models.ForeignKey(LeadSheetsMasterNew,on_delete=models.CASCADE,null=True,blank=True)
    scopeof_average = models.CharField(max_length=50, blank=True)
    time_taken = models.CharField(max_length=50, blank=True,null=True)
    def __str__(self):
        return (self.program_name)

