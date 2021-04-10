from django import forms
from django.contrib.auth import authenticate

from .models import User

class UserForm(forms.ModelForm):
    email = forms.EmailField(
        label='email',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    username = forms.CharField(
        label="username",
        required=True,
        widget = forms.TextInput(
            attrs = {
                'class':'form-control'
            }
        )
    )

    name = forms.CharField(
        label="name",
        required=True,
        widget = forms.TextInput(
            attrs = {
                'class':'form-control'
            }
        )
    )

    lastname = forms.CharField(
        label="lastname",
        required=True,
        widget = forms.TextInput(
            attrs = {
                'class':'form-control'
            }
        )
    )

    password1 = forms.CharField(
        label="password",
        required=True,
        widget = forms.PasswordInput(
            attrs = {
                'class':'form-control'
            }
        )
    )

    password2 = forms.CharField(
        label="confirm password",
        required=True,
        widget = forms.PasswordInput(
            attrs = {
                'class':'form-control'
            }
        )
    )

    class Meta:
        model = User
        fields = (
            "email",
            "username",
            "name",
            "lastname"
        )

    def clean_password2(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            self.add_error("password2", "the passwords do not match")

class LoginForm(forms.Form):
    email = forms.EmailField(
        label='email',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder':'email',
                'class':'form-control'
            }
        )
    )

    password = forms.CharField(
        label='password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'password',
                'class':'form-control'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('the email or password is wrong')    
        
        return cleaned_data