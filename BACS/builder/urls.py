from django.urls import path
from builder.views import *
from . import views

# BUILDER'S SECTION
urlpatterns = [
    path('dashboard/', views.dashboard_builder, name='builder_dashboard'),
    path('add_projects/', views.add_projects, name='add_projects'),  
    path('project_list/', views.project_list, name='project_list'), 
    path('add_type/',views.add_type,name='add_type'),
    path('create_user/',views.create_user,name='create_user'),
    path('client_list/',views.client_list,name='client_list'),
    path('assign_shareholder/',views.assign_shareholder,name='assign_shareholder'),
    path('assign_shareholder_list/',views.project_wise_shareholder_list,name='assign_shareholder_list'),
    path('add_cost_category/',views.add_cost_category,name='add_cost_category'),
    path('add_cost/',views.add_cost,name='add_cost'),
    path('add_collected_amount/',views.add_collected_amount,name='add_collected_amount'),
    path('collected_amount_statement/',views.collected_amount_list,name='collected_amount_list'),
]