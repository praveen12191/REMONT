from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile
# adding the Email fields so we can inherite the existing fild and add email to it
class useregister(UserCreationForm):
    email = forms.EmailField()

  
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
# for updating the user infoo

"""class user_uptade(forms.ModelForm):
    email = forms.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = forms.CharField(validators=[phone_regex], max_length=17)
    class Meta:
        model = User
        fields = ['username','email']"""

class user_uptade(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']
class profile_update(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image']
