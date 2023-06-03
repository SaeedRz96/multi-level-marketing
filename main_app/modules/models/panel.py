from django.db import models
from django.contrib.auth.models import User
import random
import string


def key_generator():
    key = ''.join(random.choice(string.digits) for x in range(6))
    if Panel.objects.filter(code=key).exists():
        key = key_generator()
    return key


class Panel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    code = models.CharField(max_length=6, default=key_generator, unique=True, primary_key=True)
    title = models.CharField(max_length=1000, default='پنل من')
    description = models.TextField(null=True,blank=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
