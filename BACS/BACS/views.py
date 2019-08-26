from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail,EmailMultiAlternatives
from django.utils.html import strip_tags
from django.contrib.auth.models import User,Group
import random
from . import settings


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            if request.user.groups.filter(name="builder").exists():
                # user is belongs to account group
                return redirect("/builder/dashboard/")
            elif request.user.groups.filter(name="client").exists():
                return redirect("/client/dashboard/")
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("Wrong Password or Username"))
            return HttpResponseRedirect(reverse('login'))
    else:
        return render(request,'login/login.html')


def logout_view(request):
    logout(request)
    return redirect("/")

def forgot_password(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        print(user_name)
        email = request.POST.get('email')
        user_email = User.objects.filter(email=email)
        if user_email:
            str_Key='bacs'           
            str_RandomKey =''                                                                                        
            for int_I in range(15):                                                                                    
                str_RandomKey = random.choice('0123456789')
                randomKey =  str_Key + str_RandomKey
            print(randomKey)
            body_string = 'Your New Password is: %s' % (randomKey)
            update_password = User.objects.get(username=user_name)
            update_password.set_password(randomKey)
            update_password.save()
            # send_mail('New password',body_string,settings.DEFAULT_FROM_EMAIL, [user_email],fail_silently=False)
            msg = EmailMultiAlternatives('New Password', body_string, settings.DEFAULT_FROM_EMAIL, [email])
            msg.send()
            messages.add_message(request, messages.SUCCESS, 'PLease Login Again')
            return HttpResponseRedirect(reverse('login'))
        else:
            messages.add_message(request, messages.ERROR, 'Wrong Email Address')
            return HttpResponseRedirect(reverse('login'))
        return render(request,'forgot_password.html')
    else:
        return render(request,'forgot_password.html')