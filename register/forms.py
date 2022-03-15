from logging import PlaceHolder
from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#FOR DROPDOWNS
CATEGORY = (
    ('', 'Category'),
    ('MF', 'Manufacturer'),
    ('RF', 'Refurbisher'),
    ('RC', 'Recycler')
)

class RegisterForm(UserCreationForm):
    category =  forms.ChoiceField(choices=CATEGORY)
    # category = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Category'}))
    company_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Company Name'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Location'}))
    admin_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'F_name L_name'}))
    # username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    # password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['category'].label = ''
        # self.fields['category'].empty_label = None
        self.fields['company_name'].label = ''
        self.fields['location'].label = ''
        self.fields['admin_name'].label = ''
        self.fields['username'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''
        
    class Meta:
        model = User
        fields = ["category", "company_name", "location", "admin_name", "username", "password1", "password2"]