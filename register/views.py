from winreg import REG_SZ
from django.shortcuts import redirect, render
from .forms import RegisterForm

# Create your views here.
def register1(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('/user')
    else:
        form = RegisterForm()

    return render(response, 'register.html', {'form': form})