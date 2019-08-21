from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User,Group
from builder.models import *

# Create your views here.

def dashboard_client(request):
	projects = ShareholderList.objects.filter(user=request.user).count()
	print(projects)
	total_amount = 0
	given_amount = CollectedAmount.objects.filter(from_user = request.user.id)
	for i in given_amount:
		total_amount += i.amount
	print(total_amount)
	datas = CollectedAmount.objects.filter(from_user=request.user.id)
	total_given_amount = 0
	for i in datas:
		total_given_amount += i.amount
	context = {
		'projects':projects,
		'total_amount':total_amount,
		'datas':datas,
		'total_given_amount':total_given_amount,
	}
	return render(request,'clients/dashboard.html',context)

def update_profile(request):
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		password = request.POST.get('password')
		confirm_password = request.POST.get('confirm_password')

		if password == confirm_password:
			data = User.objects.filter(id=request.user.id).update(first_name=first_name,last_name=last_name)
			update_password = User.objects.get(id=request.user.id)
			update_password.set_password(password)
			update_password.save()
			messages.add_message(request, messages.SUCCESS, 'PLease Login Again')
			return HttpResponseRedirect(reverse('login'))
		else:
			messages.add_message(request, messages.ERROR, 'Password did not match !')
			return HttpResponseRedirect(reverse('update_profile'))
	else:
		data = User.objects.filter(id=request.user.id)
		print(data)
		return render(request,'clients/update_profile.html',{'data':data})

def my_profile(request):
	data = User.objects.filter(id=request.user.id)

	return render(request,'clients/my_profile.html',{'data':data})

def view_given_amount(request):
	if request.method == 'POST':
		project_id = request.POST.get('project')
		datas = CollectedAmount.objects.filter(for_project=project_id)
		total_given_amount = 0
		for i in datas:
			total_given_amount += i.amount
		context = {
			'datas':datas,
			'total_given_amount':total_given_amount,
		}
		return render(request, 'clients/view_given_amount_report.html',context)
	else:
		projects = ShareholderList.objects.filter(user=request.user.id)
		context = {
			'projects':projects,
		}
		return render(request, 'clients/view_given_amount.html',context)
		
def given_amount(request):
	datas = CollectedAmount.objects.filter(from_user=request.user.id)
	total_given_amount = 0
	for i in datas:
		total_given_amount += i.amount

	context = {
		'datas':datas,
		'total_given_amount':total_given_amount,
	}
	return render(request,'clients/given_amount.html',context)


def view_cost_info(request):
	if request.method == 'POST':
		project_id = request.POST.get('project')
		datas = Cost.objects.filter(for_project=project_id)
		print(datas)
		total_cost = 0
		for i in datas:
			total_cost += i.cost
		context = {
			'datas':datas,
			'total_cost':total_cost,
		}
		return render(request,'clients/view_cost_info_report.html',context)
	else:
		projects = ShareholderList.objects.filter(user=request.user.id)
		context = {
			'projects':projects,
		}
		return render(request,'clients/view_cost_info.html',context)