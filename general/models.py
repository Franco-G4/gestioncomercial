from django.db import models

# Create your models here.
class Productos(models.Model):
    codigo = models.CharField(primary_key=True, max_length=70)
    idcategoria = models.ForeignKey('Categorias', on_delete = models.CASCADE)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    costo_unitario = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    utilidad = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    precioventa = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    descuento = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    importeiva = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    fechaultima = models.DateField(blank=True, null=True)
    unidad = models.CharField(max_length=50, blank=True, null=True)
    stock = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    stock_minimo = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    control_stock = models.BooleanField(blank=True, null=True)
    stock_detallado = models.BooleanField(blank=True, null=True)
    imagen = models.BinaryField(blank=True, null=True)
    
    def __str__(self):
        return self.descripcion
    
class Categorias(models.Model):
    idcategoria = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=70, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
   
    def __str__(self):
        return self.descripcion
