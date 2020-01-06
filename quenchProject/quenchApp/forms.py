from django.forms import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class Sign_Up_UserForm(ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password']

class Sign_In_UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']


