from enum import unique
import re
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms import formsets
from django.forms.widgets import Textarea

from django.utils.translation import ugettext_lazy as _
from builder.models import *


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

class ProjectsForm(forms.ModelForm):
	class Meta:
		model = Projects
		fields = '__all__'

class ShareHolderForm(forms.ModelForm):
	class Meta:
		model = ShareholderList
		fields = '__all__'