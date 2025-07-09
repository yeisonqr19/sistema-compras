from django.contrib import admin
from inventario.models import Categoria

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    admin.site.register(Categoria)