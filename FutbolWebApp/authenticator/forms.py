from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=50, label='Email')
    first_name = forms.CharField(required=True, max_length=50, label='First name')
    last_name = forms.CharField(required=True, max_length=50, label='Last name')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']