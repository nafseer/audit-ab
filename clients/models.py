# # Create your models here.
# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.utils import timezone
# from django.shortcuts import render
# from django.contrib.auth.signals import user_logged_in, user_logged_out
# from django.dispatch import receiver
# from datetime import datetime

# class DesignationMaster(models.Model):
#     client_designation = models.CharField(max_length=50, null=True,blank=True)
#     def __str__(self):
#         return str(self.client_designation)

# class RolesMaster(models.Model):
#     client_role = models.CharField(max_length=50, null=True,blank=True)
#     def __str__(self):
#         return str(self.client_role)


# class ClientsMaster(models.Model):
    
#     client_engagement = models.CharField(max_length=150, blank=True)
#     client_company = models.CharField(max_length=150, blank=True)
#     client_cin = models.CharField(max_length=150, blank=True)
#     client_address = models.CharField(max_length=200, blank=True)
#     client_doi = models.DateTimeField(default=timezone.now,null=True,blank=True)
#     client_teamname = models.CharField(max_length=200, blank=True)
#     client_designation = models.ForeignKey(DesignationMaster,on_delete=models.CASCADE,null=True,blank=True,related_name='sample1')
#     client_role = models.ForeignKey(RolesMaster,on_delete=models.CASCADE,null=True,blank=True,related_name='sample2')
#     client_name = models.CharField(max_length=150, blank=True)
#     client_position = models.CharField(max_length=150, blank=True)
#     client_email = models.CharField(max_length=150, blank=True)
#     client_phone = models.CharField(max_length=150, blank=True)

#     def __str__(self):
#         return (self.client_name)



    


