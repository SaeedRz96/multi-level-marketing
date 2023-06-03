from rest_framework.serializers import ModelSerializer
from main_app.modules.models import CreditModel

class Credit(ModelSerializer):
    class Meta:
        model = CreditModel
        fields = '__all__'