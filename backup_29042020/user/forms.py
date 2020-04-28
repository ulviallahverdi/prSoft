from django.forms import ModelForm
#from user.models import Register
from django import forms
from django.contrib.auth.models import User

class RegisterForm(ModelForm):
    username = forms.CharField(max_length=25)
    password = forms.CharField(max_length=25,widget=forms.PasswordInput())
    confirm = forms.CharField(max_length=25,widget=forms.PasswordInput())

    def clean(self):
        password = self.cleaned_data["password"]
        confirm = self.cleaned_data["confirm"]
        username = self.cleaned_data["username"]

        if password != confirm:
            raise forms.ValidationError("Passwords don't match")
        return {
            "password":password,
            "confirm":confirm,
            "username":username
        }
    class Meta:
        model = User
        fields = ["username","password","confirm"]