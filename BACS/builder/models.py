from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserType(models.Model):
	name = models.CharField(max_length=50,blank=True,null=True)
	created_at = models.DateField(auto_now_add=True,blank=True)
	updated_at = models.DateField(auto_now_add=True,blank=True)

class Projects(models.Model):
	pname = models.CharField(max_length=150,blank=True,null=True)
	building_name = models.CharField(max_length=150,blank=True,null=True)
	address = models.CharField(max_length=255,blank=True,null=True)
	builders_name = models.CharField(max_length=150,blank=True,null=True)
	builders_address = models.CharField(max_length=150,blank=True,null=True)
	created_by = models.ForeignKey('auth.User',blank=True,null=True,on_delete=models.CASCADE)
	created_at = models.DateField(auto_now_add=True,blank=True)
	updated_at = models.DateField(auto_now_add=True,blank=True)

class ShareholderList(models.Model):
	user = models.ForeignKey('auth.User',blank=True,null=True,on_delete=models.CASCADE)
	projects = models.ForeignKey('builder.Projects',blank=True,null=True,on_delete=models.CASCADE)
	created_by = models.ForeignKey('auth.User',blank=True,null=True,on_delete=models.CASCADE,related_name='builder')
	created_at = models.DateField(auto_now_add=True,blank=True)

class ClientUser(models.Model):
	user_type = models.ForeignKey('builder.UserType',blank=True,null=True, on_delete=models.CASCADE)
	user = models.ForeignKey('auth.User', blank=True, null=True, on_delete=models.CASCADE, related_name='client_user')
	created_by = models.ForeignKey('auth.User',blank=True,null=True,on_delete=models.CASCADE)
	created_at = models.DateField(auto_now_add=True,blank=True)