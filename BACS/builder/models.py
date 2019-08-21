from django.contrib.auth.models import User,Group
from django.db import models
from decimal import Decimal

# Create your models here.

class UserType(models.Model):
	name = models.CharField(max_length=50,blank=True,null=True)
	created_at = models.DateField(auto_now_add=True,blank=True)
	updated_at = models.DateField(auto_now_add=True,blank=True)
	
	def __str__(self):
		return self.name

class Projects(models.Model):
	pname = models.CharField(max_length=150,blank=True,null=True)
	building_name = models.CharField(max_length=150,blank=True,null=True)
	address = models.CharField(max_length=255,blank=True,null=True)
	builders_name = models.CharField(max_length=150,blank=True,null=True)
	builders_address = models.CharField(max_length=150,blank=True,null=True)
	estimated_cost = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal(0.00), null=True, blank=True)
	duration = models.CharField(max_length=55,blank=True,null=True)
	total_floor = models.IntegerField(blank=True,null=True)
	created_by = models.ForeignKey('auth.User',blank=True,null=True,on_delete=models.CASCADE)
	created_at = models.DateField(auto_now_add=True,blank=True)
	updated_at = models.DateField(auto_now_add=True,blank=True)

	def __str__(self):
		return self.pname

class ShareholderList(models.Model):
	user = models.ForeignKey('auth.User',blank=True,null=True,on_delete=models.CASCADE)
	projects = models.ForeignKey('builder.Projects',blank=True,null=True,on_delete=models.CASCADE)
	created_by = models.ForeignKey('auth.User',blank=True,null=True,on_delete=models.CASCADE,related_name='builder')
	created_at = models.DateField(auto_now_add=True,blank=True)

	def __str__(self):
		return self.user.username

class ClientUser(models.Model):
	user_type = models.ForeignKey('auth.Group',blank=True,null=True, on_delete=models.CASCADE)
	user = models.ForeignKey('auth.User', blank=True, null=True, on_delete=models.CASCADE, related_name='client_user')
	created_by = models.ForeignKey('auth.User',blank=True,null=True,on_delete=models.CASCADE)
	created_at = models.DateField(auto_now_add=True,blank=True)

class CostCategory(models.Model):
	category = models.CharField(max_length=100, blank=True, null=True)
	created_by = models.ForeignKey('auth.User',blank=True,null=True,on_delete=models.CASCADE,related_name='category_creator')
	created_at = models.DateField(auto_now_add=True,blank=True)

	def __str__(self):
		return self.category

class Cost(models.Model):
	cost_info = models.CharField(max_length=150,blank=True,null=True)
	cost = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal(0.00), null=True, blank=True)
	cost_category = models.ForeignKey('builder.CostCategory',blank=True,null=True,on_delete=models.CASCADE)
	for_project = models.ForeignKey('builder.Projects',blank=True,null=True,related_name='projects_cost',on_delete=models.CASCADE)
	created_by = models.ForeignKey('auth.User',blank=True,null=True,on_delete=models.CASCADE,related_name='cost_inserter')
	created_at = models.DateField(auto_now_add=True,blank=True)

class CollectedAmount(models.Model):
	amount = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal(0.00), null=True, blank=True)
	from_user = models.ForeignKey('auth.User',blank=True,null=True,related_name='from_user',on_delete=models.CASCADE)
	for_project = models.ForeignKey('builder.Projects',blank=True,null=True,related_name='for_project',on_delete=models.CASCADE)
	created_by = models.ForeignKey('auth.User',blank=True,null=True,related_name='collected_by',on_delete=models.CASCADE)
	date = models.DateField(blank=True,null=True)
	created_at = models.DateField(auto_now_add=True,blank=True,null=True)

	def __str__(self):
		return self.from_user.username