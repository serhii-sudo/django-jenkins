from django.urls import path

from apps.clients.views import Home

urlpatterns = [
    path('data/', Home.as_view(), name='data'),
]