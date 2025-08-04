from django.shortcuts import render

from django.db import models
# importing models 
from django.contrib.auth.models import User
# importing User model

# Create your views here.

class UserProfile(models.Model):
    user = models.OneToOneField(User ,on_delete =models.CASCADE ,related_name = 'profile')
    name =models.CharField(max_length =255)
    email =models.EmailField()
    phone_number =models.CharField(max_length =255)


    def __str__(self):
        return self.name
