from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import UserRegistrationForm

# Create your views here.
class VSignUp(View):

    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'signUp.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('main:index')
            else:
                for msg in form.error_messages:
                    messages.error(request, form.error_messages[msg])
                return render(request, 'signUp.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('main:index')
            else:
                messages.error(request,'Credentials do not match any user in the system')
        else:
            messages.error(request, 'Credentials do not match any user in the system')

    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def log_out(request):
    logout(request)
    return redirect('main:index')