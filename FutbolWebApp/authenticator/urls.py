from django.urls import path
from . import views

app_name = 'authenticator'

urlpatterns = [
    path('login', views.log_in, name='login'),
    path('sign-up', views.VSignUp.as_view(), name='signUp'),
    path('logout', views.log_out, name='logout'),
]