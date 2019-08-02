from django.urls import path
from builder.views import *
from . import views

# BUILDER'S SECTION
urlpatterns = [
    path('dashboard/', views.dashboard_builder, name='builder_dashboard'),
    path('add_projects/', views.add_projects, name='add_projects'),  
    path('project_list/', views.project_list, name='project_list'),
    path('delete_project/<pid>', views.delete_project, name="delete_project"),
    path('edit_project/<pid>', views.edit_project, name="edit_project"),
    path('add_type/',views.add_type,name='add_type'),
    path('create_user/',views.create_user,name='create_user'),
    path('client_list/',views.client_list,name='client_list'),
    path('delete_client/<uid>', views.delete_client, name="delete_client"),
    path('edit_client/<uid>', views.edit_client, name="edit_client"),
    path('assign_shareholder/',views.assign_shareholder,name='assign_shareholder'),
    path('assign_shareholder_list/',views.project_wise_shareholder_list,name='assign_shareholder_list'),
    path('delete_assigned_shareholder/<sid>',views.delete_assigned_shareholder,name='delete_assigned_shareholder'),
    path('add_cost_category/',views.add_cost_category,name='add_cost_category'),
    path('add_cost/',views.add_cost,name='add_cost'),
    path('cost_info_list/',views.cost_info_list,name='cost_info_list'),
    path('delete_cost_info/<cid>',views.delete_cost_info,name='delete_cost_info'),
    path('edit_cost_info/<cid>',views.edit_cost_info,name='edit_cost_info'),
    path('add_collected_amount/',views.add_collected_amount,name='add_collected_amount'),
    path('collected_amount_statement/',views.collected_amount_list,name='collected_amount_list'),
    path('delete_collected_amount/<cid>',views.delete_collected_amount,name='delete_collected_amount'),
    path('edit_collected_amount/<cid>',views.edit_collected_amount,name='edit_collected_amount'),
]