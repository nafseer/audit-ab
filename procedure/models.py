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
from company.models import CompanyList



class ProcedureMaster(models.Model):
    company_name = models.CharField(max_length=50, blank=True)
    auditee_name = models.CharField(max_length=50, null=True,blank=True)
    started_on = models.CharField(max_length=200,null=True)
    completed_on = models.CharField(max_length=200,null=True)
    reviewer = models.CharField(max_length=50, null=True,blank=True)
    reviewed_on = models.CharField(max_length=200,null=True)
    time_taken = models.CharField(max_length=200,null=True)
    # notesfile = models.FileField(null=True)
    # comments = models.CharField(max_length=400, null=True,blank=True)
 
    def __str__(self):
        return (self.auditee_name)

class ProcedureFile(models.Model):
    company_name = models.CharField(max_length=50, blank=True)
    notesfile = models.FileField(null=True)

    def __str__(self):
        return (self.company_name)

class ProcedureComments(models.Model):
    company_name = models.CharField(max_length=50, blank=True)
    comments = models.CharField(max_length=400, null=True,blank=True)
    def __str__(self):
        return (self.comments)
 



    


