from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('categoria/<int:categoria_id>/', views.articulos_por_categoria, name='categoria'),
    # Nueva URL para ver el detalle del producto:
    path('articulo/<int:articulo_id>/', views.detalle_articulo, name='detalle_articulo'),
]