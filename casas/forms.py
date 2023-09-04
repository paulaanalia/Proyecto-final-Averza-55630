from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CasaForm(forms.Form):
    calle = forms.CharField(max_length=50, required=True)
    altura = forms.IntegerField(required=True)
    piso = forms.IntegerField()
    departamento = forms.CharField(max_length=50)
    localidad = forms.CharField(max_length=50, required=True)
    horario = forms.TimeField(required=True)
    anfitrion = forms.CharField(max_length=50, required=True)
    menu = forms.CharField(max_length=100, required=True)



class RegistroForm(UserCreationForm):      
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EditForm(UserCreationForm):
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput) 
    first_name = forms.CharField(label="Nombre", max_length=50, required=False)   
    last_name = forms.CharField(label="Apellido", max_length=50, required=False)   

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name'] 

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)