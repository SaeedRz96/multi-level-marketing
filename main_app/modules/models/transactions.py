from django.db import models
from main_app.modules.models import CreditModel


class Transactions(models.Model):
    credit = models.ForeignKey(CreditModel,on_delete=models.CASCADE)
    ACTIVITY_CHOICES = [
        ('income', 'Income'),
        ('outcome', 'Outcome'),
    ]
    activity = models.CharField(
        max_length=10,
        choices=ACTIVITY_CHOICES,
    )
    amount = models.BigIntegerField()
    sell_history = models.CharField(max_length=10,default=0)
    description = models.TextField(null=True,blank=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

