from django.contrib.admin import ModelAdmin, register

from main_app.modules.models import *


@register(PanelModel)
class PanelAdmin(ModelAdmin):
    pass


@register(LevelModel)
class LevelAdmin(ModelAdmin):
    pass


@register(CoWorkersModel)
class CoWorkersAdmin(ModelAdmin):
    pass


@register(SellHistoryModel)
class SellHistoryAdmin(ModelAdmin):
    pass


@register(CreditModel)
class CreditAdmin(ModelAdmin):
    pass


@register(TransactionsModel)
class TransactionsAdmin(ModelAdmin):
    pass


@register(ProfileModel)
class ProfileAdmin(ModelAdmin):
    pass