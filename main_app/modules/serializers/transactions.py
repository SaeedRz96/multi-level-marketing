from rest_framework.serializers import ModelSerializer
from main_app.modules.models import TransactionsModel

class Transactions(ModelSerializer):
    class Meta:
        model = TransactionsModel
        fields = '__all__'