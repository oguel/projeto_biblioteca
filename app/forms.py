from django import forms
from .models import Livro, Genero, Editora, Autor, Emprestimo, UF, Cidade, Usuario

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'
    
class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = '__all__'

class EditoraForm(forms.ModelForm):
    class Meta:
         model = Editora
         fields = '__all__'

class UFForm(forms.ModelForm):
    class Meta:
         model = UF
         fields = '__all__'

class CidadeForm(forms.ModelForm):
    class Meta:
         model = Cidade
         fields = '__all__'
        
class UsuarioForm(forms.ModelForm):
    class Meta:
         model = Usuario
         fields = '__all__'

class EmprestimoForm(forms.ModelForm):
    class Meta:
         model = Emprestimo
         fields = '__all__'


