from django.db import models
from main_app.modules.models import CoWorkersModel


class SellHistory(models.Model):
    coworker = models.ForeignKey(CoWorkersModel , on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    description = models.TextField(null=True,blank=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)