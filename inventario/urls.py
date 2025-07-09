from django.urls import path
from inventario.views import CategoriaView, CategoriaNew, CategoriaEdit, CategoriaDelete

app_name = "inventario"

urlpatterns = [
    path("categorias/", CategoriaView.as_view(), name="categorias"),
    path("categoria/new", CategoriaNew.as_view(),name="categoria-new"),
    path("categoria/edit/<int:pk>", CategoriaEdit.as_view(), name="categoria-edit"),
    path("categoria/delete/<int:pk>", CategoriaDelete.as_view(), name="categoria-delete"),
]
