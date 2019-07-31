from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.contrib.auth import authenticate
from django.http.response import HttpResponse, HttpResponseRedirect
from builder.forms.forms import *
from django.contrib.auth.models import User,Group

# Create your views here.

def dashboard_builder(request):
	return render(request,'builder/dashboard.html')

def add_projects(request):
	"""
	Add New Porjects. Builder's Administration will add this projectss
	:param request:
	:return: 
	"""
	form = ProjectsForm()
	if request.method == 'POST':
		form = ProjectsForm(request.POST or None)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			data = Projects.objects.last()
			print(data.id)
			update_data = Projects.objects.filter(id=data.id).update(created_by=request.user)
			messages.add_message(request, messages.SUCCESS, 'SuccessFully Add New Projects')
			return HttpResponseRedirect(reverse('add_projects'))
	return render(request,'builder/add_projects.html',{'form':form})

def project_list(request):
	data = Projects.objects.filter(created_by=request.user)

	context = {
		'project_datas':data,
	}
	return render(request,'builder/project_list.html',context)

def add_type(request):
	if request.method == 'POST':
		type_name = request.POST.get('type_name')
		data = Group.objects.create(name=type_name)
		data.save()
		messages.add_message(request, messages.SUCCESS, 'SuccessFully Added')
		return HttpResponseRedirect(reverse('add_type'))
	else:
		return render(request,'builder/add_type.html')

def create_user(request):
    if request.method == 'POST':
    	user_name = request.POST.get('user_name')
    	user_password = request.POST.get('user_password')
    	user_email = request.POST.get('user_email')
    	user_type = request.POST.get('user_type')
    	print(user_email)
    	if len(user_name) > 0 and len(user_password) > 0 and len(user_email) > 0:
    		user = authenticate(request, username=user_name, password=user_password)
    		if user is None:
    			user = User.objects.create_user(username=user_name, password=user_password, email=user_email)
    			user.is_staff = True
    			user.save()
    			groups = Group.objects.get(id=user_type)
    			last_user = User.objects.last()
    			user_data = ClientUser.objects.create(user_type=groups,user=last_user,created_by=request.user)
    			last_user.groups.add(groups)
    			messages.add_message(request, messages.SUCCESS, 'SuccessFully Added')
    		else:
    			messages.add_message(request, messages.ERROR, 'This is already in User List')
    		return HttpResponseRedirect(reverse('builder_dashboard'))
    	else:
    		messages.add_message(request, messages.ERROR, 'ERROR !! Not Added ')
    	return render(request,'builder/create_user.html')
    else:
    	user_type = Group.objects.all()
    	context = {
    		'user_type':user_type,
    	}
    	return render(request,'builder/create_user.html',context)

def client_list(request):
	get_client = ClientUser.objects.filter(created_by=request.user)
	print(get_client)
	context = {
		'all_clients':get_client,
	}
	return render(request,'builder/client_list.html',context)

def assign_shareholder(request):
	form = ShareholderList()
	if request.method == 'POST':
		projects_name = request.POST.get('project')
		user_name = request.POST.get('user')
		user = User.objects.filter(id=user_name).first()
		projects = Projects.objects.filter(id=projects_name).first()
		data = ShareholderList.objects.create(user=user,projects=projects,created_by=request.user)
		messages.add_message(request, messages.SUCCESS, 'SuccessFully Assigned !!')
		return HttpResponseRedirect(reverse('assign_shareholder'))
	else:
		all_projects = Projects.objects.filter(created_by=request.user.id)
		all_clients = ClientUser.objects.filter(created_by=request.user.id)

		context = {
			'all_projects':all_projects,
			'all_clients':all_clients,
			'form':form,
		}
		return render(request,'builder/assign_shareholder.html',context)

def project_wise_shareholder_list(request):
	datas = ShareholderList.objects.filter(created_by=request.user.id)
	print(datas)
	context = {
		'datas':datas,
	}
	return render(request,'builder/project_wise_user_list.html',context)


def add_cost_category(request):
	if request.method == 'POST':
		category_name = request.POST.get('category_name')
		data = CostCategory.objects.create(category=category_name,created_by=request.user)
		messages.add_message(request, messages.SUCCESS, 'SuccessFully Assigned !!')
		return HttpResponseRedirect(reverse('add_cost_category'))
	else:
		return render(request,'builder/add_cost_category.html')

def add_cost(request):
	if request.method == 'POST':
		cost_info = request.POST.get('cost_info')
		cost = request.POST.get('cost')
		cost_category = request.POST.get('category')
		project_id = request.POST.get('project')
		print(cost_category)
		category_id = CostCategory.objects.filter(id=cost_category).first()
		project = Projects.objects.filter(id=project_id).first()
		data = Cost.objects.create(cost_info=cost_info,cost=cost,cost_category=category_id,created_by=request.user,for_project=project)
		messages.add_message(request, messages.SUCCESS, 'SuccessFully Cost Added !!')
		return HttpResponseRedirect(reverse('add_cost'))
	else:
		cost_categories = CostCategory.objects.filter(created_by=request.user.id)
		projects = Projects.objects.filter(created_by=request.user)
		context = {
			'cost_categories':cost_categories,
			'projects':projects,
		}
		return render(request,'builder/add_cost.html',context)

def add_collected_amount(request):
	if request.method == "POST":
		amount = request.POST.get('amount')
		shareholder = request.POST.get('shareholder')
		print(shareholder)
		project = request.POST.get('project')
		date = request.POST.get('date')
		shareholder_name = User.objects.filter(id=shareholder).first()
		project_name = Projects.objects.filter(id=project).first()

		data = CollectedAmount.objects.create(amount=amount,from_user=shareholder_name,for_project=project_name,created_by=request.user,date=date)

		messages.add_message(request, messages.SUCCESS, 'SuccessFully Amount Added !!')
		return HttpResponseRedirect(reverse('add_collected_amount'))
	else:
		print(request.user)
		user_list = ShareholderList.objects.filter(created_by=request.user)
		project_list = Projects.objects.filter(created_by=request.user)

		context = {
			'user_list':user_list,
			'project_list':project_list,
		}
		return render(request,'builder/collected_amount.html',context)

def collected_amount_list(request):
	if request.method == 'POST':
		project_id = request.POST.get('project')
		print(project_id)
		datas = CollectedAmount.objects.filter(for_project=project_id)
		total_collected_amount = 0
		for i in datas:
			total_collected_amount += i.amount

		context = {
			'datas':datas,
			'total_collected_amount':total_collected_amount,
		}
		return render(request,'builder/collected_amount_report.html',context)
	else:
		projects = Projects.objects.filter(created_by=request.user)
		print(projects)
		return render(request,'builder/collected_amount_statement.html',{'projects':projects})