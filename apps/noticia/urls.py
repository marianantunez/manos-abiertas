from django.urls import path
from .views import NoticiaListView, NoticiaDetalleView

urlpatterns = [
    path("noticias", NoticiaListView.as_view()),
    path('detalle/<int:pk>', NoticiaDetalleView.as_view(), name='detalle'),
]