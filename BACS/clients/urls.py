from django.urls import path
from clients.views import *
from . import views

# CLIENTS SECTION
urlpatterns = [
    path('dashboard/', views.dashboard_client, name='client_dashboard'),
]