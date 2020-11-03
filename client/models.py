# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from datetime import datetime

class DesignationMasterNew(models.Model):
    client_designation = models.CharField(max_length=50, null=True,blank=True)
    def __str__(self):
        return str(self.client_designation)

class RolesMasterNew(models.Model):
    client_role = models.CharField(max_length=50, null=True,blank=True)
    def __str__(self):
        return str(self.client_role)


class ClientsProfile(models.Model):
    
    company_name = models.CharField(max_length=50, null=True,blank=True)
    client_company = models.CharField(max_length=150, null=True,blank=True)
    client_cin = models.CharField(max_length=150, null=True,blank=True)
    client_address = models.CharField(max_length=200, null=True,blank=True)
    client_doi = models.CharField(max_length=200,null=True,blank=True)
    # client_teamname = models.CharField(max_length=200, null=True,blank=True)
    # client_designation = models.ForeignKey(DesignationMasterNew,on_delete=models.CASCADE,null=True,blank=True,related_name='sample3')
    # client_role = models.ForeignKey(RolesMasterNew,on_delete=models.CASCADE,null=True,blank=True,related_name='sample4')
    # client_name = models.CharField(max_length=150, null=True,blank=True)
    # client_position = models.CharField(max_length=150, null=True,blank=True)
    # client_email = models.CharField(max_length=150, null=True,blank=True)
    # client_phone = models.CharField(max_length=150, null=True,blank=True)

    def __str__(self):
        return str(self.client_company)

class ClientsTeam(models.Model):
    company_name = models.CharField(max_length=50, null=True,blank=True)
    client_teamname = models.CharField(max_length=200, null=True,blank=True)
    client_designation = models.ForeignKey(DesignationMasterNew,on_delete=models.CASCADE,null=True,blank=True,related_name='sample3')
    client_role = models.ForeignKey(RolesMasterNew,on_delete=models.CASCADE,null=True,blank=True,related_name='sample4')

    def __str__(self):
        return str(self.client_teamname)
    
class ClientsContact(models.Model):
    company_name = models.CharField(max_length=50, null=True,blank=True)
    client_name = models.CharField(max_length=150, null=True,blank=True)
    client_position = models.CharField(max_length=150, null=True,blank=True)
    client_email = models.CharField(max_length=150, null=True,blank=True)
    client_phone = models.CharField(max_length=150, null=True,blank=True)

    def __str__(self):
        return str(self.client_name)


