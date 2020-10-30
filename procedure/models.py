# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from datetime import datetime
from django.utils import timezone



class ProcedureMaster(models.Model):
    auditee_name = models.CharField(max_length=50, null=True,blank=True)
    started_on = models.DateTimeField(default=timezone.now,null=True,blank=True)
    completed_on = models.DateTimeField(default=timezone.now,null=True,blank=True)
    reviewer = models.CharField(max_length=50, null=True,blank=True)
    reviewed_on = models.DateTimeField(default=timezone.now,null=True,blank=True)
    time_taken = models.DateTimeField(default=timezone.now,null=True,blank=True)
    notesfile = models.FileField(null=True)
    comments = models.CharField(max_length=400, null=True,blank=True)
 
    def __str__(self):
        return (self.auditee_name)




    


