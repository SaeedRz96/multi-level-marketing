from rest_framework.serializers import ModelSerializer
from main_app.modules.models import PanelModel

class Panel(ModelSerializer):
    class Meta:
        model = PanelModel
        fields = '__all__'