from django.urls import path
from main_app.modules.views import (
    SellHistoryListCreateApiView,
    SellHistoryRetrieveUpdateDestroyApiView
)

app_name = 'main_app_sell_history'
urlpatterns = [
    path('', SellHistoryListCreateApiView.as_view(), name='list_create'),
    path('/<int:pk>', SellHistoryRetrieveUpdateDestroyApiView.as_view(), name='retrieve_update_destroy'),
]