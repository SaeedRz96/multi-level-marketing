from rest_framework import generics
from main_app.modules.serializers import CreditSerializer
from main_app.modules.models import CreditModel

class Credit():
    queryset = CreditModel.objects.all()
    serializer_class = CreditSerializer


class ListCreate(Credit,generics.ListCreateAPIView):...


class RetrieveUpdateDestroy(Credit,generics.RetrieveUpdateDestroyAPIView):...