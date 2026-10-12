from django.db import models

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombrecategoria = models.CharField(max_length=100)
    imagencategoria = models.ImageField(upload_to='img/categorias/', verbose_name="Imagen Categoría", null=True, blank=True)

    def __str__(self):
        return self.nombrecategoria

class Material(models.Model):
    id_material = models.AutoField(primary_key=True)
    nombrematerial = models.CharField(max_length=100)
    imagenmaterial = models.ImageField(upload_to='img/materiales/', verbose_name="Imagen Material", null=True, blank=True)

    def __str__(self):
        return self.nombrematerial

class Articulo(models.Model):
    id_articulo = models.AutoField(primary_key=True)
    nombrearticulo = models.CharField(max_length=100)
    
    # Aquí está la magia de Django: ForeignKeys en lugar de IntegerField
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoría")
    material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name="Material")
    
    imagen1 = models.ImageField(upload_to='img/articulos/', verbose_name="Imagen 1", null=True, blank=True)
    imagen2 = models.ImageField(upload_to='img/articulos/', verbose_name="Imagen 2", null=True, blank=True)
    imagen3 = models.ImageField(upload_to='img/articulos/', verbose_name="Imagen 3", null=True, blank=True)
    imagen4 = models.ImageField(upload_to='img/articulos/', verbose_name="Imagen 4", null=True, blank=True)
    
    largo = models.IntegerField(verbose_name="Largo (cm)")
    ancho = models.IntegerField(verbose_name="Ancho (cm)")
    alto = models.IntegerField(verbose_name="Alto (cm)")
    
    visible = models.BooleanField(verbose_name="Visible", default=True)
    reservado = models.BooleanField(verbose_name="Reservado", default=False)
    stock = models.IntegerField(verbose_name="Stock")

    def __str__(self):
        return self.nombrearticulo
