from django.shortcuts import render, redirect
from .forms import FormularioRegistro, noticiasForm
from django.contrib.auth import authenticate, login


def principal(request):
    return render(request, "index.html")

def nosotros(request):
    return render(request,"nosotros.html")

def registro(request):
    data = {
        'form': FormularioRegistro()
    }
    if request.method == 'POST':
        formulario = FormularioRegistro(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request,user)
            return redirect(to='home')
        data['form'] = formulario
    return render(request,'registration/registro.html',data)
    
def agregar_noticias(request):
    data = {
        'form': noticiasForm()
    }
    if request.method == 'POST':
        formulario = noticiasForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']= 'guardado correctamente'
        else:
            data['mensaje']= formulario    
        
    return render(request, 'noticias/agregar_noticias.html', data)

