from django.urls import path
from main_app.modules.views import (
    LevelListCreateApiView,
    LevelRetrieveUpdateDestroyApiView
)

app_name = 'main_app_level'
urlpatterns = [
    path('', LevelListCreateApiView.as_view(), name='list_create'),
    path('/<int:pk>', LevelRetrieveUpdateDestroyApiView.as_view(), name='retrieve_update_destroy'),
]