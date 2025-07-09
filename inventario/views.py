from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from inventario.models import Categoria
from inventario.forms import CategoriaForm

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