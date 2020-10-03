from django.forms import ModelForm
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class order_form(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class user_registeration_form(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']

class user_settings(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']