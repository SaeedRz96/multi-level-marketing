from rest_framework import generics
from main_app.modules.serializers import SellHistorySerializer
from main_app.modules.models import SellHistoryModel, CreditModel, CoWorkersModel,TransactionsModel

from rest_framework import status
from rest_framework.response import Response

class SellHistory():
    queryset = SellHistoryModel.objects.all()
    serializer_class = SellHistorySerializer


class ListCreate(SellHistory,generics.ListCreateAPIView):
    
    def perform_create(self, serializer):
        obj = serializer.save()
        credit = CreditModel.objects.get(coworker = obj.coworker)
        credit.number_of_sell = credit.number_of_sell + 1
        if obj.coworker.personal_commission == -1:
            commission = round(obj.amount * (obj.coworker.level.commission)/100)
            up_level_commission = obj.amount - commission
            credit.cash_amount = credit.cash_amount + commission
        else:
            commission = round(obj.amount * (obj.coworker.personal_commission)/100)
            up_level_commission = obj.amount - commission
            credit.cash_amount = credit.cash_amount + commission
        credit.total_amount = credit.cash_amount + credit.child_profits
        credit.save()
        transaction = TransactionsModel()
        transaction.credit = credit
        transaction.activity = 'income'
        transaction.amount = commission
        transaction.sell_history = obj.id
        transaction.description = 'an income transaction'
        transaction.save()
        parent = obj.coworker.parent
        while parent != '0' :
            up_level = CoWorkersModel.objects.get(code=parent)
            up_level_credit = CreditModel.objects.get(coworker = up_level)
            up_level_credit.number_of_child_sell = up_level_credit.number_of_child_sell + 1
            if up_level.personal_commission == -1:
                commission = round(up_level_commission * (up_level.level.commission)/100)
                up_level_commission = up_level_commission - commission
                up_level_credit.child_profits = up_level_credit.child_profits + commission
            else:
                commission = round(up_level_commission * (up_level.personal_commission)/100)
                up_level_commission = up_level_commission - commission
                up_level_credit.child_profits = up_level_credit.child_profits + commission
            up_level_credit.total_amount = up_level_credit.cash_amount + up_level_credit.child_profits
            up_level_credit.save()
            transaction = TransactionsModel()
            transaction.credit = up_level_credit
            transaction.activity = 'income'
            transaction.amount = commission
            transaction.sell_history = obj.id
            transaction.description = 'an income transaction'
            transaction.save()
            parent = up_level.parent




class RetrieveUpdateDestroy(SellHistory,generics.RetrieveUpdateDestroyAPIView):

    def perform_update(self, serializer):
        obj = serializer.save()
        if 'amount' in serializer.data:
            credit = CreditModel.objects.get(coworker = obj.coworker)
            transaction = TransactionsModel.objects.get(credit = credit,sell_history=obj.id)
            credit.cash_amount = credit.cash_amount - transaction.amount
            credit.save()
            if obj.coworker.personal_commission == -1:
                commission = round(obj.amount * (obj.coworker.level.commission)/100)
                up_level_commission = obj.amount - commission
                credit.cash_amount = credit.cash_amount + commission
            else:
                commission = round(obj.amount * (obj.coworker.personal_commission)/100)
                up_level_commission = obj.amount - commission
                credit.cash_amount = credit.cash_amount + commission
            credit.total_amount = credit.cash_amount + credit.child_profits
            credit.save()
            transaction.amount = commission
            transaction.save()
            parent = obj.coworker.parent
            while parent != '0' :
                up_level = CoWorkersModel.objects.get(code=parent)
                up_level_credit = CreditModel.objects.get(coworker = up_level)
                transaction = TransactionsModel.objects.get(credit = up_level_credit,sell_history=obj.id)
                up_level_credit.child_profits = up_level_credit.child_profits - transaction.amount
                up_level_credit.save()
                if up_level.personal_commission == -1:
                    commission = round(up_level_commission * (up_level.level.commission)/100)
                    up_level_commission = up_level_commission - commission
                    up_level_credit.child_profits = up_level_credit.child_profits + commission
                else:
                    commission = round(up_level_commission * (up_level.personal_commission)/100)
                    up_level_commission = up_level_commission - commission
                    up_level_credit.child_profits = up_level_credit.child_profits + commission
                up_level_credit.total_amount = up_level_credit.cash_amount + up_level_credit.child_profits
                up_level_credit.save()
                transaction.amount = commission
                transaction.save()
                parent = up_level.parent

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        credit = CreditModel.objects.get(coworker = instance.coworker)
        transaction = TransactionsModel.objects.get(credit = credit,sell_history=instance.id)
        credit.cash_amount = credit.cash_amount - transaction.amount
        credit.number_of_sell = credit.number_of_sell - 1
        credit.total_amount = credit.cash_amount + credit.child_profits
        credit.save()
        transaction.delete()
        parent = instance.coworker.parent
        while parent != '0' :
            up_level = CoWorkersModel.objects.get(code=parent)
            up_level_credit = CreditModel.objects.get(coworker = up_level)
            transaction = TransactionsModel.objects.get(credit = up_level_credit,sell_history=instance.id)
            up_level_credit.number_of_child_sell = up_level_credit.number_of_child_sell - 1
            up_level_credit.child_profits = up_level_credit.child_profits - transaction.amount
            up_level_credit.total_amount = up_level_credit.cash_amount + up_level_credit.child_profits
            up_level_credit.save()
            transaction.delete()
            parent = up_level.parent
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
