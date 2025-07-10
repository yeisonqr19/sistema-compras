from django import forms
from inventario.models import Categoria, SubCategoria, Marca

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