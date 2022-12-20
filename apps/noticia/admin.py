from django.contrib import admin
from.models import Noticia, Categoria

@admin.register(Noticia)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'id','activo','fecha','categoria')

admin.site.register(Categoria)    
# Register your models here.
