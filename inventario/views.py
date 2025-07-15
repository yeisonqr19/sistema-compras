from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from inventario.models import Categoria, SubCategoria, Marca, UnidadesMedidas, Producto
from inventario.forms import CategoriaForm, SubCategoriaForm, MarcaForm, UnidadesMedidasForm, ProductosForm

class CategoriaView(LoginRequiredMixin, ListView):
    
    model = Categoria
    template_name = "inventario/lista_categoria.html"
    context_object_name = "categorias"
    login_url = "/login/"
    
class CategoriaNew(LoginRequiredMixin,CreateView):
    
    model = Categoria
    template_name = "inventario/add_categoria.html"
    login_url = "/login/"
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

class MarcaView(LoginRequiredMixin, ListView):
    
    model = Marca
    template_name = "inventario/lista_marcas.html"
    context_object_name = "marcas"
    login_url = "/login/"
    
class MarcaAdd(LoginRequiredMixin, CreateView):
    
    model = Marca
    template_name = "inventario/add_marca.html"
    login_url = "/login/"
    form_class = MarcaForm
    success_url = reverse_lazy("inventario:marcas")
    
    def form_valid(self, form):
        form.instance.ucreacion = self.request.user
        return super().form_valid(form)
    
class MarcaEdit(LoginRequiredMixin, UpdateView):
    model = Marca
    template_name = "inventario/add_marca.html"
    context_object_name = "marca"
    form_class = MarcaForm
    success_url = reverse_lazy("inventario:marcas")
    
    def form_valid(self, form):
        form.instance.umodificacion = self.request.user.id
        return super().form_valid(form)

@login_required
def marca_disable(request,marca_id):

    marca = get_object_or_404(Marca, id = marca_id)
    
    ctx = {
        'marca':marca,
    }
    
    if request.method == "POST":
        marca.estado = False
        marca.save()
        return redirect("inventario:marcas")
    
    return render(request, "inventario/disable_marca.html", ctx)
    
@login_required
def marca_enable(request, marca_id):
    
    marca = get_object_or_404(Marca, id = marca_id)
    
    template_name = "inventario/enable_marca.html"
    ctx = {
        'marca':marca,
    }
    
    if request.method == "POST":
        marca.estado = True
        marca.save()
        return redirect("inventario:marcas")
    
    return render(request, template_name, ctx)

class UniMedidasView(LoginRequiredMixin, ListView):
     model = UnidadesMedidas
     login_url = "/login/"
     template_name = "inventario/lista_unidadesmedidas.html"
     context_object_name = "unimedidas"
     
class UniMedidasAdd(LoginRequiredMixin, CreateView):
    model = UnidadesMedidas
    login_url = "/login/"
    template_name = "inventario/add_unidadesmedidas.html"
    form_class = UnidadesMedidasForm
    success_url = reverse_lazy("inventario:unimedidas")
    
    def form_valid(self, form):
        form.instance.ucreacion = self.request.user
        return super().form_valid(form)
    
class UniMedidasEdit(LoginRequiredMixin, UpdateView):
    model = UnidadesMedidas
    login_url = "/login/"
    template_name = "inventario/add_unidadesmedidas.html"
    form_class = UnidadesMedidasForm
    success_url = reverse_lazy("inventario:unimedidas")
    context_object_name = "unimedida"
    
    def form_valid(self, form):
        form.instance.umodificacion = self.request.user.id
        return super().form_valid(form)

@login_required
def unimedida_disable(request, unimedida_id):
    
    unimedida = get_object_or_404(UnidadesMedidas, id = unimedida_id)
    
    ctx = {
        'unimedida' : unimedida,
    }
    
    if request.method == "POST":
        unimedida.estado = False
        unimedida.save()
        return redirect("inventario:unimedidas")
    
    return render(request, "inventario/disable_unimedida.html", ctx)


@login_required
def unimedida_enable(request, unimedida_id):
    
    unimedida = get_object_or_404(UnidadesMedidas, id = unimedida_id)
    
    ctx = {
        'unimedida':unimedida,
    }
    
    if request.method == "POST":
        unimedida.estado = True
        unimedida.save()
        return redirect("inventario:unimedidas")
    
    return render(request, "inventario/enable_unimedida.html", ctx)

class ProductoView(LoginRequiredMixin, ListView):
    
    model = Producto
    login_url = "/login/"
    template_name = "inventario/lista_productos.html"
    context_object_name = "productos"
    

class ProductoAdd(LoginRequiredMixin, CreateView):
    
    model = Producto
    login_url = "/login/"
    template_name = "inventario/add_producto.html"
    success_url = reverse_lazy("inventario:productos")
    form_class = ProductosForm
    
    def form_valid(self, form):
        form.instance.ucreacion = self.request.user
        return super().form_valid(form)
    
class ProductoEdit(LoginRequiredMixin, UpdateView):
    
    model = Producto
    login_url = "/login/"
    template_name = "inventario/add_producto.html"
    context_object_name = "producto"
    success_url = reverse_lazy("inventario:productos")
    form_class = ProductosForm
    
    def form_valid(self, form):
        form.instance.umodificacion = self.request.user.id
        return super().form_valid(form)
    
@login_required
def producto_disable(request, producto_id):
    
    producto = get_object_or_404(Producto, id=producto_id)
    
    ctx = {
        'producto':producto,
    }
    
    if request.method == "POST":
        producto.estado = False
        producto.save()
        return redirect("inventario:productos")

    return render(request, "inventario/disable_producto.html", ctx)

@login_required
def producto_enable(request, producto_id):
    
    producto = get_object_or_404(Producto, id = producto_id)
    
    ctx = {
        'producto':producto,
    }
    
    if request.method == "POST":
        producto.estado = True
        producto.save()
        return redirect("inventario:productos")
    
    return render(request, "inventario/enable_producto.html", ctx)
    