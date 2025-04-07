from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','password','role']

class LoginForm(forms.Form):
    email = forms.EmailField(label="Correo Electrónico", max_length=100)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    email = forms.EmailField(label="Correo Electrónico", max_length=100)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=[('user', 'Usuario'), ('admin', 'Administrador')], required=False)