from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Modelo(models.Model):
    
    estado = models.BooleanField(default=True)
    fcreacion = models.DateTimeField(auto_now_add=True)
    fmodificacion = models.DateTimeField(auto_now=True)
    ucreacion = models.ForeignKey(User, on_delete=models.CASCADE)
    umodificacion = models.IntegerField(null=True, blank=True)
    
    class Meta:
        abstract = True
    
    