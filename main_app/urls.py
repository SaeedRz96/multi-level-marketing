from django.urls import path, include
from .views import *

app_name = 'main_app'
urlpatterns = [
    path('api/v1/panel', include('main_app.modules.urls.panel')),
    path('api/v1/level', include('main_app.modules.urls.level')),
    path('api/v1/coworkers', include('main_app.modules.urls.coworkers')),
    path('api/v1/credit', include('main_app.modules.urls.credit')),
    path('api/v1/sell-history', include('main_app.modules.urls.sell_history')),
    path('api/v1/transactions', include('main_app.modules.urls.transactions')),
]
