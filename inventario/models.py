from django.db import models
from home.models import Modelo

# Create your models here.

class Categoria (Modelo):
    
    descripcion = models.CharField(max_length=100, help_text="Descripcion de la nueva categoria", unique=True)
    
    def __str__(self):
        return f'{self.descripcion}'
    
    def save(self, **args):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save(**args)
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "categorias"
        
class SubCategoria(Modelo):
    
    categoriapadre = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    
    descripcion = models.CharField(max_length=100, help_text="Descripcion de la nueva subcategoria")
    
    def __str__(self):
        if self.categoriapadre:
            return f"{self.categoriapadre.descripcion} > {self.descripcion}"    
        return f"Sin Categoria Padre > {self.descripcion}"
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()
        
    class Meta:
        verbose_name = "sub categoria"
        verbose_name_plural = "Sub categorias"
        unique_together = ('categoriapadre', 'descripcion')
        
class Marca(Modelo):
    
    descripcion = models.CharField(max_length=100, help_text="Nombre de la marca", unique=True)
    
    def __str__(self):
        return f'{self.descripcion}'
    
    def save(self, **args):
        self.descripcion = self.descripcion.upper()
        super(Marca, self).save(**args)
    
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        
class UnidadesMedidas(Modelo):
    
    descripcion = models.CharField(max_length=100, help_text="Nombre de la unidad", unique=True)
    
    def __str__(self):
        return f'{self.descripcion}'
    
    def save(self, **args):
        self.descripcion = self.descripcion.upper()
        super(UnidadesMedidas, self).save(**args)
    
    class Meta:
        verbose_name = "Unidad de medida"
        verbose_name_plural = "Unidades de medidas"
        
class Producto(Modelo):
    
    codigo = models.CharField(max_length=20, unique=True)
    codigo_barra = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.FloatField(default=0)
    existencia_producto = models.IntegerField(default=0)
    ultima_compra = models.DateField(null=True, blank=True)
    
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(UnidadesMedidas, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.descripcion}"
    
    def save(self, **args):
        self.descripcion = self.descripcion.upper()
        super(Producto, self).save(**args)
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        unique_together = ('codigo', 'codigo_barra')