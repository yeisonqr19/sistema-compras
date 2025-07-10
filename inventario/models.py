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