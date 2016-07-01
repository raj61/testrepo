from __future__ import unicode_literals

from django.db import models
from django import forms
# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_name','password']
