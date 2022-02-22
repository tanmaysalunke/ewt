from logging import PlaceHolder
from django import forms

# STATES = (
#     ('', 'Choose...'),
#     ('MG', 'Minas Gerais'),
#     ('SP', 'Sao Paulo'),
#     ('RJ', 'Rio de Janeiro')
# )

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)

