from rest_framework import routers
from . import api_views
from django.urls import path, include
from builder.views import *
router = routers.DefaultRouter()


urlpatterns = [
	path('projectList', api_views.ProjectList.as_view(),name='projects_api'),
    path('userList', api_views.ProjectWiseClientListAPI.as_view(), name="project_wise_client_list"),
]