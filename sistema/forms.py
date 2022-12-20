from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.noticia.models import Noticia



class FormularioRegistro(UserCreationForm): 
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', ]       
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control"}),
            'first_name': forms.TextInput(attrs={"class": "form-control"}),
            'last_name': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'password1': forms.PasswordInput(attrs={"class": "form-control"}),
            'password2': forms.PasswordInput(attrs={"class": "form-control"}),
        }

class noticiasForm(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = '__all__'
        widgets = {
            'texto': forms.Textarea(attrs={"class": "form-control"}),
            'titulo': forms.TextInput(attrs={"class": "form-control"}),
            'subtitulo': forms.Textarea(attrs={"class": "form-control"}),
            'publicado': forms.SelectDateWidget(attrs={"class": "form-control"}),
            'categoria': forms.Select(attrs={"class": "form-control"}),
           
        }
