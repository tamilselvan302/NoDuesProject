from django.contrib.auth.models import User
from django import forms

class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    class meta:
        model = User
        fields = ['username','password']