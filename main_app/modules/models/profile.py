from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    national_code = models.CharField(max_length=10, null=True,blank=True)
    phone_number = models.CharField(max_length=20, null=True,blank=True)