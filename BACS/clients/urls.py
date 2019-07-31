from django.urls import path
from clients.views import *
from . import views

# CLIENTS SECTION
urlpatterns = [
    path('dashboard/', views.dashboard_client, name='client_dashboard'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('view_given_amount/', views.view_given_amount, name='view_given_amount'),
    path('view_cost_info/', views.view_cost_info, name='view_cost_info'),
]