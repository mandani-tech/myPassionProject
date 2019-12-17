from django.forms import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class NewUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']