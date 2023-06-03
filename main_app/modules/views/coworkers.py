from rest_framework import generics
from main_app.modules.serializers import CoWorkersSerializer
from main_app.modules.models import CoWorkersModel,CreditModel

class CoWorker():
    queryset = CoWorkersModel.objects.all()
    serializer_class = CoWorkersSerializer


class ListCreate(CoWorker,generics.ListCreateAPIView):
    def perform_create(self, serializer):
        obj = serializer.save()
        credit = CreditModel()
        credit.coworker = obj
        credit.save()


class RetrieveUpdateDestroy(CoWorker,generics.RetrieveUpdateDestroyAPIView):...