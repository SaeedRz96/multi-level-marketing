from rest_framework.serializers import ModelSerializer
from main_app.modules.models import LevelModel

class Level(ModelSerializer):
    class Meta:
        model = LevelModel
        fields = '__all__'