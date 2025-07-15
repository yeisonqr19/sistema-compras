from django import forms
from inventario.models import Categoria, SubCategoria, Marca, UnidadesMedidas, Producto

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']
        labels = {'descripcion':"categoria", 'estado':"Estado"}
        widget = {'descripcion': forms.TextInput}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})
            
class SubCategoriaForm(forms.ModelForm):
    class Meta:
        model = SubCategoria
        fields = ['categoriapadre','descripcion', 'estado']
        labels = {'descripcion':"Sub Categoria", 'estado':"Estado"}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})    

        self.fields['categoriapadre'].empty_label = "Seleccione Categoria"
        
class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['descripcion', 'estado']
        labels = {'descripcion':"Marca", 'estado':"Estado"}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})
                
class UnidadesMedidasForm(forms.ModelForm):
    class Meta:
        model = UnidadesMedidas
        fields = ['descripcion', 'estado']
        labels = {'descripcion':'Descripcion de medida', 'estado':'estado'}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})
            
class ProductosForm(forms.ModelForm):
    class Meta:
        model = Producto
        field = ['codigo', 'codigo_barra', 'descripcion', 'estado', 'precio', 'existencia_producto', 'ultima_compra', 'marca', 'subcategoria', 'unidad_medida']
        
        exclude = ['umodificacion','fmodificacion','ucreacion','fcreacion']
        
        widget = {'descripcion': forms.TextInput()}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })
        self.fields['ultima_compra'].widget.attrs['readonly'] = True
        self.fields['existencia_producto'].widget.attrs['readonly'] = True
        