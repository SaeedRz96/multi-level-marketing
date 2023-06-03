from django.db import models
from main_app.modules.models import CoWorkersModel


class Credit(models.Model):
    coworker = models.OneToOneField(CoWorkersModel, on_delete=models.CASCADE)
    number_of_sell = models.IntegerField(default=0)
    cash_amount = models.BigIntegerField(default=0)
    number_of_child_sell = models.IntegerField(default=0)
    child_profits = models.BigIntegerField(default=0)
    total_amount = models.BigIntegerField(default=0)
    def __str__(self) -> str:
        return '{} {}'.format(self.coworker.first_name,self.coworker.last_name)