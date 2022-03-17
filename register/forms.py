from logging import PlaceHolder
from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UsernameField

#FOR DROPDOWNS
CATEGORY = (
    ('', 'Category'),
    ('MF', 'Manufacturer'),
    ('RF', 'Refurbisher'),
    ('RC', 'Recycler')
)

class RegisterForm(UserCreationForm):
    category =  forms.ChoiceField(choices=CATEGORY, required=True)
    # category = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Category'}))
    company_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}))
    
    first_name = forms.CharField(max_length=12, min_length=4, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=12, min_length=4, required=True, widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})))
    email = forms.EmailField(max_length=50, widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email ID'})))

    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}))
    # admin_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'F_name L_name'}))
    username = UsernameField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'id': 'username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'id': 'password1'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password', 'id': 'password2'}))
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['category'].label = ''
        # self.fields['category'].empty_label = None
        self.fields['company_name'].label = ''
        self.fields['location'].label = ''
        # self.fields['admin_name'].label = ''
        self.fields['first_name'].label = ''
        self.fields['email'].label = ''
        self.fields['last_name'].label = ''
        self.fields['username'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "category", "company_name", "location", "username", "password1", "password2"]

