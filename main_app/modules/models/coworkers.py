from django.db import models 
from main_app.modules.models import LevelModel
import random
import string


def key_generator():
    key = ''.join(random.choice(string.digits) for x in range(6))
    if CoWorkers.objects.filter(code=key).exists():
        key = key_generator()
    return key


class CoWorkers(models.Model):
    parent = models.CharField(max_length=6,default=0)
    level = models.ForeignKey(LevelModel,on_delete=models.CASCADE)
    code = models.CharField(max_length=6, default=key_generator, unique=True, primary_key=True)
    first_name = models.CharField(max_length=1000, null=True,blank=True)
    last_name = models.CharField(max_length=1000, null=True,blank=True)
    national_code = models.CharField(max_length=10, null=True,blank=True)
    phone_number = models.CharField(max_length=20, null=True,blank=True)
    extra_info = models.TextField(null=True,blank=True)
    personal_commission = models.IntegerField(default=-1)
    modified_date = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

