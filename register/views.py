from winreg import REG_SZ
from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.db import IntegrityError
from django.http.response import StreamingHttpResponse
from django.shortcuts import render, redirect
from datetime import date
from django.http import JsonResponse
import time
from django.http import HttpResponse

# Create your views here.
# def register1(response):
#     if response.method == "POST":
#         form = RegisterForm(response.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/login')
#     else:
#         form = RegisterForm()

#     return render(response, 'register/register.html', {'form': form})


# LOGIN
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('register')
        else:
            messages.info(request, 'Username or Password is incorrect')
    return render(request, 'registration/login.html')


# LOGOUT
@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')


# REGISTRATION
# @login_required(login_url='login')
def registerPage(request):
    if request.method == 'POST':
        user_reg = User.objects.create_user(first_name=request.POST.get('first_name'),
                        last_name=request.POST.get('last_name'),
                        password=request.POST.get('password1'),
                        # password2=request.POST.get('password2'),
                        email=request.POST.get('email'),
                        username=request.POST.get('username'),
                        location=request.POST.get('location'),
                        company_name=request.POST.get('company_name'),
                        )
        try:
            user_reg.save()
            groups = Group.objects.get(name=request.POST.get('access_level'))
            groups.user_set.add(user_reg)
            # request.session['regname'] = request.POST.get('first_name')
            # context = {'folder_name': request.POST.get('first_name')}
            return render(request, "registration/login.html")
        except IntegrityError:
            messages.info(request, "Username already present!")
    return render(request, 'register/register.html')
# # TABLE DATA
# @login_required(login_url='login')
# def table_data(request):
#     records = logs.objects.all().order_by('-VISIT_TIME')
#     count = logs.objects.count()
#     lock_status = request.session['lock']
#     return render(request, 'smart_lock/logs.html', {'records': records, 'count': count, 'lock_status':lock_status})
