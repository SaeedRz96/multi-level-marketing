from rest_framework import generics
from main_app.modules.serializers import TransactionsSerializer
from main_app.modules.models import TransactionsModel
from rest_framework import status
from rest_framework.response import Response

class Transactions():
    queryset = TransactionsModel.objects.all()
    serializer_class = TransactionsSerializer


class ListCreate(Transactions,generics.ListCreateAPIView):

    def perform_create(self, serializer):
        obj = serializer.save()
        credit = obj.credit
        if obj.activity == 'income':
            credit.total_amount = credit.total_amount + obj.amount
        elif obj.activity == 'outcome':
            credit.total_amount = credit.total_amount - obj.amount
        credit.save()

class RetrieveUpdateDestroy(Transactions,generics.RetrieveDestroyAPIView):

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.sell_history == '0':
            credit = instance.credit
            credit.total_amount = credit.total_amount - instance.amount
            credit.save()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
    def perform_destroy(self, instance):
        instance.delete()