from rest_framework import generics
from main_app.modules.serializers import LevelSerializer
from main_app.modules.models import LevelModel

class Level():
    queryset = LevelModel.objects.all()
    serializer_class = LevelSerializer


class ListCreate(Level,generics.ListCreateAPIView):...


class RetrieveUpdateDestroy(Level,generics.RetrieveUpdateDestroyAPIView):...