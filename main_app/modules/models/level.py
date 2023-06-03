from django.db import models
from main_app.modules.models import PanelModel


class Level(models.Model):
    panel = models.ForeignKey(PanelModel,on_delete=models.CASCADE)
    level_number = models.PositiveIntegerField()
    title = models.CharField(max_length=1000, null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    commission = models.PositiveIntegerField()
    modified_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)