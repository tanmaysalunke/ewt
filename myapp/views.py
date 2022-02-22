from urllib import request
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import LoginForm
from .models import UIDS
#from django.views.generic import CreateView
#from .models import user

# Create your views here.
def login(request):
    return render(request, 'login.html', {'name': 'Tanmay'})

def register(request):  
    return render(request, 'register.html', {'name': 'Tanmay'})

# def user(request):
#     form = CustomerForm()
#     return render(request, 'customer_form.html', {'form' : form})
    #fields = ('category', 'company_name', 'location', 'admin_name', 'username', 'password', 'cnf_password')

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/base/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def add(request):
    val1= int(request.POST["num1"])
    val2= int(request.POST["num2"])
    sum= val1+ val2

    return render(request, "result.html", {'result': sum})

def ref(request):
    uid1= UIDS()
    uid1.uid = 1234

    uid2= UIDS()
    uid2.uid = 2345

    uid3= UIDS()
    uid3.uid = 3456

    uid4= UIDS()
    uid4.uid = 4567

    uidss = [uid1, uid2, uid3, uid4]

    return render(request, "ref.html", {'uidss': uidss})