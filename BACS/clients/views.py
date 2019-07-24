from django.shortcuts import render

# Create your views here.

def dashboard_client(request):
	return render(request,'clients/index.html')