from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from inventario.models import Categoria, SubCategoria
from inventario.forms import CategoriaForm, SubCategoriaForm

class CategoriaView(LoginRequiredMixin, ListView):
    
    model = Categoria
    template_name = "inventario/lista_categoria.html"
    context_object_name = "categorias"
    login_url = "/login/"
    
class CategoriaNew(LoginRequiredMixin,CreateView):
    
    model = Categoria
    template_name = "inventario/add_categoria.html"
    login_url = "/login/"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("inventario:categorias") 

    def form_valid(self, form):
        form.instance.ucreacion = self.request.user
        return super().form_valid(form)
    

class CategoriaEdit(LoginRequiredMixin,UpdateView):
    
    model = Categoria
    template_name = "inventario/add_categoria.html"
    login_url = "/login/"
    context_object_name = "categoria"
    form_class = CategoriaForm
    success_url = reverse_lazy("inventario:categorias")
    
    def form_valid(self, form):
        form.instance.umodificacion = self.request.user.id
        return super().form_valid(form)

class CategoriaDelete(LoginRequiredMixin, DeleteView):
    
    model = Categoria
    template_name = "inventario/borrar_categorias.html"
    context_object_name = "categoria"
    login_url = "/login/"
    success_url = reverse_lazy("inventario:categorias")
    
class SubCategoriaView(LoginRequiredMixin,ListView):
    
    model = SubCategoria
    template_name = "inventario/lista_subcategoria.html"
    context_object_name = "subcategorias"
    login_url = "/login/"
    
class SubCategoriaAdd(LoginRequiredMixin,CreateView):
    model = SubCategoria
    template_name = "inventario/add_subcategoria.html"
    context_object_name = "subcategoria"
    login_url = "/login/"
    form_class = SubCategoriaForm
    success_url = reverse_lazy("inventario:subcategorias")
    
    def form_valid(self, form):
        form.instance.ucreacion = self.request.user
        return super().form_valid(form)
    
        
class SubCategoriaEdit(LoginRequiredMixin, UpdateView):
    model = SubCategoria
    template_name = "inventario/add_subcategoria.html"
    login_url = "/login/"
    context_object_name = "subcategoria"
    form_class = SubCategoriaForm
    success_url = reverse_lazy("inventario:subcategorias")
    
    def form_valid(self, form):
        form.instance.umodificacion = self.request.user.id
        return super().form_valid(form)
    
class SubCategoriaDelete(LoginRequiredMixin, DeleteView):
    model = SubCategoria
    template_name = "inventario/borrar_subcategorias.html"
    login_url = "/login/"
    context_object_name = "subcategoria"
    success_url = reverse_lazy("inventario:subcategorias")


