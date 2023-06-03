from rest_framework.serializers import ModelSerializer
from main_app.modules.models import CoWorkersModel

class CoWorkers(ModelSerializer):
    class Meta:
        model = CoWorkersModel
        fields = '__all__'