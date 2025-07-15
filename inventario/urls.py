from django.urls import path
from inventario.views import CategoriaView, CategoriaNew, CategoriaEdit, CategoriaDelete, SubCategoriaView, SubCategoriaAdd, SubCategoriaEdit, SubCategoriaDelete, MarcaView, MarcaAdd, MarcaEdit, marca_disable, marca_enable, UniMedidasView, UniMedidasAdd, UniMedidasEdit,unimedida_disable, unimedida_enable, ProductoView, ProductoAdd, ProductoEdit, producto_enable, producto_disable

app_name = "inventario"

urlpatterns = [
    path("categorias/", CategoriaView.as_view(), name="categorias"),
    path("categorias/new", CategoriaNew.as_view(),name="categoria-new"),
    path("categoria/edit/<int:pk>", CategoriaEdit.as_view(), name="categoria-edit"),
    path("categoria/delete/<int:pk>", CategoriaDelete.as_view(), name="categoria-delete"),
    
    path("subcategorias/", SubCategoriaView.as_view(), name="subcategorias"),
    path("subcategorias/new",SubCategoriaAdd.as_view(), name="subcategoria-new"),
    path("subcategorias/edit/<int:pk>", SubCategoriaEdit.as_view(), name="subcategoria-edit"),
    path("subcategorias/delete/<int:pk>",SubCategoriaDelete.as_view(), name="subcategoria-delete"),
    
    path("marcas/", MarcaView.as_view(), name= "marcas"),
    path("marcas/new",MarcaAdd.as_view(),name="marca-new"),
    path("marcas/edit/<int:pk>", MarcaEdit.as_view(), name="marca-edit"),
    path("marcas/disable/<int:marca_id>", marca_disable , name="marca-disable"),
    path("marcas/enable/<int:marca_id>", marca_enable, name="marca-enable"),
    
    path("unimedidas/", UniMedidasView.as_view(), name="unimedidas"),
    path("unimedidas/new", UniMedidasAdd.as_view(), name="unimedida-new"),
    path("unimedidas/edit/<int:pk>", UniMedidasEdit.as_view(), name="unimedida-edit"),
    path("unimedidas/disable/<int:unimedida_id>",unimedida_disable, name="unimedida-disable"),
    path("unimedidas/enable/<int:unimedida_id>",unimedida_enable, name="unimedida-enable"),
    
    path("productos/", ProductoView.as_view(), name="productos"),
    path("productos/new",ProductoAdd.as_view(), name="producto-new" ),
    path("productos/edit/<int:pk>", ProductoEdit.as_view(), name="producto-edit"),
    path("productos/disable/<int:producto_id>", producto_disable, name="producto-disable"),
    path("productos/enable/<int:producto_id>", producto_enable, name="producto-enable"),
    
    
]
