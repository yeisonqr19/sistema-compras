from django.urls import path
from inventario.views import CategoriaView, CategoriaNew, CategoriaEdit, CategoriaDelete, SubCategoriaView, SubCategoriaAdd, SubCategoriaEdit, SubCategoriaDelete, MarcaView, MarcaAdd, MarcaEdit, marca_disable, marca_enable

app_name = "inventario"

urlpatterns = [
    path("categorias/", CategoriaView.as_view(), name="categorias"),
    path("categoria/new", CategoriaNew.as_view(),name="categoria-new"),
    path("categoria/edit/<int:pk>", CategoriaEdit.as_view(), name="categoria-edit"),
    path("categoria/delete/<int:pk>", CategoriaDelete.as_view(), name="categoria-delete"),
    
    path("subcategorias/", SubCategoriaView.as_view(), name="subcategorias"),
    path("subcategoria/new",SubCategoriaAdd.as_view(), name="subcategoria-new"),
    path("subcategoria/edit/<int:pk>", SubCategoriaEdit.as_view(), name="subcategoria-edit"),
    path("subcategoria/delete/<int:pk>",SubCategoriaDelete.as_view(), name="subcategoria-delete"),
    
    path("marcas/", MarcaView.as_view(), name= "marcas"),
    path("marca/new",MarcaAdd.as_view(),name="marca-new"),
    path("marca/edit/<int:pk>", MarcaEdit.as_view(), name="marca-edit"),
    path("marca/disable/<int:marca_id>", marca_disable , name="marca-disable"),
    path("marca/enable/<int:marca_id>", marca_enable, name="marca-enable"),
    
]
