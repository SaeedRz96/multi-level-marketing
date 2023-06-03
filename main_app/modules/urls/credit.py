from django.urls import path
from main_app.modules.views import (
    CreditListCreateApiView,
    CreditRetrieveUpdateDestroyApiView
)

app_name = 'main_app_credit'
urlpatterns = [
    path('', CreditListCreateApiView.as_view(), name='list_create'),
    path('/<int:pk>', CreditRetrieveUpdateDestroyApiView.as_view(), name='retrieve_update_destroy'),
]