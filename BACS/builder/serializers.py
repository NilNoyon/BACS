from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_bulk.drf3.serializers import BulkSerializerMixin, BulkListSerializer

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from builder.models import *

class ShareholderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareholderList
        fields = '__all__'

class ProjectsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Projects
		fields = '__all__'