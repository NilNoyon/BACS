from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout


def login_success(request):
    """
    Redirects users based on assigned groups
    """
    if request.user.groups.filter(name="builder").exists():
        # user is belongs to account group
        return redirect("/builder/dashboard/")
    elif request.user.groups.filter(name="client").exists():
        return redirect("/client/dashboard/")
    else:
        # return HttpResponse('<h3>Permission Denied</h3>')
        return redirect("/admin/")


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.groups.filter(name="builder").exists():
                # user is belongs to account group
                return redirect("/builder/dashboard/")
            elif request.user.groups.filter(name="clients").exists():
                return redirect("/client/dashboard/")
        else:
            # Return an 'invalid login' error message.
            return redirect("/")
    else:
        return render(request,'login/login.html')


def logout_view(request):
    logout(request)
    return redirect("/")