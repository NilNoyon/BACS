from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework_bulk.generics import ListBulkCreateAPIView
from builder.models import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import *
# Create your views here.

class ProjectWiseClientListAPI(APIView):

    def get(self, request):
        id = request.GET.get('id')
        print(id)
        client_list = ShareholderList.objects.filter(projects=id)
        print(client_list)
        shareholders = []
        for i in client_list:
        	shareholders.append(i.user.username)
        serializer = ShareholderListSerializer(client_list, many=True)
        response = list(zip(serializer.data, shareholders))
        print(response)
        return Response(response)

class ProjectList(APIView):

	def get(self, request, format=None):
	    snippets = Projects.objects.filter(created_by=request.user)
	    serializer = ProjectsSerializer(snippets, many=True)
	    return Response(serializer.data)
