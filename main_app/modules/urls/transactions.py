from django.urls import path
from main_app.modules.views import (
    TransactionsListCreateApiView,
    TransactionsRetrieveUpdateDestroyApiView
)

app_name = 'main_app_transactions'
urlpatterns = [
    path('', TransactionsListCreateApiView.as_view(), name='list_create'),
    path('/<int:pk>', TransactionsRetrieveUpdateDestroyApiView.as_view(), name='retrieve_update_destroy'),
]