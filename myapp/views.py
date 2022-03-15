from urllib import request
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import LoginForm, RegisterForm

#from django.views.generic import CreateView
#from .models import user

# Create your views here.
def login(request):
    form = LoginForm()
    return render(request, 'login.html', {'form': form})
    

def register(request):
    form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# def user(request):
#     form = CustomerForm()
#     return render(request, 'customer_form.html', {'form' : form})
    #fields = ('category', 'company_name', 'location', 'admin_name', 'username', 'password', 'cnf_password')
    

def add(request):
    val1= int(request.POST["num1"])
    val2= int(request.POST["num2"])
    sum= val1+ val2

    return render(request, "result.html", {'result': sum})
