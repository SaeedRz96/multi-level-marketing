from rest_framework import generics
from main_app.modules.serializers import PanelSerializer
from main_app.modules.models import PanelModel

class Panel():
    queryset = PanelModel.objects.all()
    serializer_class = PanelSerializer


class ListCreate(Panel,generics.ListCreateAPIView):...


class RetrieveUpdateDestroy(Panel,generics.RetrieveUpdateDestroyAPIView):...