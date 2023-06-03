from rest_framework.serializers import ModelSerializer
from main_app.modules.models import SellHistoryModel

class SellHistory(ModelSerializer):
    class Meta:
        model = SellHistoryModel
        fields = '__all__'