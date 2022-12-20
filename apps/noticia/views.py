from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Noticia

# Create your views here.

class NoticiaListView(ListView):
    model = Noticia
    template_name = "noticias/ListadoNoticias.html"

class NoticiaDetalleView(DetailView):
    model = Noticia
    template_name = "noticias/detalleNoticia.html"