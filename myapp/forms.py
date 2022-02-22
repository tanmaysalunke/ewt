from django import forms

STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    ) 
    address_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)


# class user(models.Model):
#     category = models.CharField(max_length=100)
#     company_name = models.CharField(max_length=200)
#     location = models.CharField(max_length=50)
#     admin_name = models.CharField(max_length=200)
#     username = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)
#     cnf_password = models.CharField(max_length=200)