from logging import PlaceHolder
from django import forms
from crispy_forms.helper import FormHelper

#FOR DROPDOWNS
CATEGORY = (
    ('', 'Category'),
    ('MF', 'Manufacturer'),
    ('RF', 'Refurbisher'),
    ('RC', 'Recycler')
)

class LoginForm(forms.Form):
    
    # email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['username'].label = ''
        self.fields['password'].label = ''

class RegisterForm(forms.Form):
    category = forms.ChoiceField(choices=CATEGORY)
    # category = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Category'}))
    company_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Company Name'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Location'}))
    admin_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'F_name L_name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}))
    cnf_password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Confirm Password'}))

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['category'].label = ''
        # self.fields['category'].empty_label = None
        self.fields['company_name'].label = ''
        self.fields['location'].label = ''
        self.fields['admin_name'].label = ''
        self.fields['username'].label = ''
        self.fields['password'].label = ''
        self.fields['cnf_password'].label = ''


# self.fields['MYFIELD'].label = False to disable for a specific field 