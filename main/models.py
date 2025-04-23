from django.db import models
from django.contrib.auth.models import User
import datetime
import time
class Website(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.text
class Username(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)#Username
    text2 = models.CharField(max_length=200)#Password
    date_added = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "Username:"+self.text+'\nPassword:'+self.text2