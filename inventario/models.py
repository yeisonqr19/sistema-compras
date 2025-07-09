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