# Create your models here.
from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.shortcuts import render
# from django.contrib.auth.signals import user_logged_in, user_logged_out
# from django.dispatch import receiver
# from datetime import datetime


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     firstname = models.CharField(max_length=50, blank=True)
#     lastname = models.CharField(max_length=50, blank=True)
#     email = models.CharField(max_length=50, blank=True)
#     phone_number = models.CharField(max_length=12, blank=True)
#     def __str__(self):
#         return '%s %s' % (self.user.first_name, self.user.last_name)


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User,dispatch_uid='save_new_user_profile')
# def save_user_profile(sender, instance,created, **kwargs):
#     instance.profile.save()    


    





