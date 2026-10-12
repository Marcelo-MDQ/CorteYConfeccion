from django.shortcuts import render, get_object_or_404
from .models import Articulo, Categoria

def inicio(request):
    categorias = Categoria.objects.all()
    articulos = Articulo.objects.filter(visible=True)
    return render(request, 'paginas/inicio.html', {  # <--- CAMBIO AQUÍ
        'categorias': categorias,
        'articulos': articulos,
        'categoria_actual': None
    })

def articulos_por_categoria(request, categoria_id):
    categorias = Categoria.objects.all()
    categoria_actual = get_object_or_404(Categoria, id_categoria=categoria_id)
    articulos = Articulo.objects.filter(categoria=categoria_actual, visible=True)
    return render(request, 'paginas/inicio.html', {  # <--- CAMBIO AQUÍ
        'categorias': categorias,
        'articulos': articulos,
        'categoria_actual': categoria_actual
    })

def detalle_articulo(request, articulo_id):
    # Traemos todas las categorías para mantener el menú superior funcionando
    categorias = Categoria.objects.all()
    # Buscamos el artículo por su ID (si no existe, da un error 404 seguro)
    articulo = get_object_or_404(Articulo, id_articulo=articulo_id)
    
    return render(request, 'paginas/detalle.html', {
        'articulo': articulo,
        'categorias': categorias
    })