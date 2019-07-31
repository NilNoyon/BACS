from django.shortcuts import render
from builder.models import *

# Create your views here.

def dashboard_client(request):
	return render(request,'clients/dashboard.html')

def update_profile(request):
	if request.method == 'POST':
		return render(request,'clients/update_profile.html')
	else:
		return render(request,'clients/update_profile.html')

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

def view_cost_info(request):
	if request.method == 'POST':
		project_id = request.POST.get('project_id')
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