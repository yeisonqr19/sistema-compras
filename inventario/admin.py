from django.contrib import admin
from inventario.models import Categoria, SubCategoria

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["descripcion"]       
    
class SubCategoriaAdmin(admin.ModelAdmin):
    list_display = ["categoriapadre", "descripcion"]

    def categoriapadre(self, obj):
    
            return obj.categoriapadre.descripcion if obj.categoriapadre else "—"

    categoriapadre.short_description = "Categoría padre" 

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(SubCategoria, SubCategoriaAdmin)