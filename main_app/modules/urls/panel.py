from django.urls import path
from main_app.modules.views import (
    PanelListCreateApiView,
    PanelRetrieveUpdateDestroyApiView
)

app_name = 'main_app_panel'
urlpatterns = [
    path('', PanelListCreateApiView.as_view(), name='list_create'),
    path('/<int:pk>', PanelRetrieveUpdateDestroyApiView.as_view(), name='retrieve_update_destroy'),
]