from django.urls import path
from main_app.modules.views import (
    CoWorkersListCreateApiView,
    CoWorkersRetrieveUpdateDestroyApiView
)

app_name = 'main_app_coworkers'
urlpatterns = [
    path('', CoWorkersListCreateApiView.as_view(), name='list_create'),
    path('/<int:pk>', CoWorkersRetrieveUpdateDestroyApiView.as_view(), name='retrieve_update_destroy'),
]