from django import forms
from .models import Cliente
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'fecha_nac', 'edad','lugar', 'foto']
        
        foto=forms.ImageField(required=False)
        
class RegistroFrom(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2' ]