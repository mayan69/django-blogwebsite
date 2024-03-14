from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class UserRegisterationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password1','password2']

    
    
    
    

    # password = forms.CharField(label="Password",max_length=50 ,min_length=5 ,widget=forms.PasswordInput)



