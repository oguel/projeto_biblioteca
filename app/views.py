from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro, Genero, Editora, Autor, Emprestimo, UF, Cidade, Usuario
from .forms import LivroForm, GeneroForm, EditoraForm, AutorForm, EmprestimoForm, UFForm, CidadeForm, UsuarioForm

# Index/Home
def index(request):
    return render(request, 'index.html')

# Livro Views
def livro_list(request):
    livros = Livro.objects.all()
    return render(request, 'livro.html', {'livros': livros})

def livro_detail(request, id):
    livro = get_object_or_404(Livro, id=id)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('livro_list')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'livro.html', {'Livro': livro, 'form': form})

# Gênero Views
def genero_list(request):
    generos = Genero.objects.all()
    return render(request, 'genero.html', {'generos': generos})

def genero_detail(request, id):
    genero = get_object_or_404(Genero, id=id)
    if request.method == 'POST':
        form = GeneroForm(request.POST, instance=genero)
        if form.is_valid():
            form.save()
            return redirect('genero_list')
    else:
        form = GeneroForm(instance=genero)
    return render(request, 'genero.html', {'genero': genero, 'form': form})

# Editora Views
def editora_list(request):
    editoras = Editora.objects.all()
    return render(request, 'editora.html', {'editoras': editoras})

def editora_detail(request, id):
    editora = get_object_or_404(Editora, id=id)
    if request.method == 'POST':
        form = EditoraForm(request.POST, instance=editora)
        if form.is_valid():
            form.save()
            return redirect('editora_list')
    else:
        form = EditoraForm(instance=editora)
    return render(request, 'editora.html', {'editora': editora, 'form': form})

# Autor Views
def autor_list(request):
    autores = Autor.objects.all()
    return render(request, 'autor.html', {'autores': autores})

def autor_detail(request, id):
    autor = get_object_or_404(Autor, id=id)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('autor_list')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'autor.html', {'autor': autor, 'form': form})

# Empréstimo Views
def emprestimo_list(request):
    emprestimos = Emprestimo.objects.all()
    return render(request, 'emprestimo.html', {'emprestimos': emprestimos})

def emprestimo_detail(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id)
    if request.method == 'POST':
        form = EmprestimoForm(request.POST, instance=emprestimo)
        if form.is_valid():
            form.save()
            return redirect('emprestimo_list')
    else:
        form = EmprestimoForm(instance=emprestimo)
    return render(request, 'emprestimo.html', {'emprestimo': emprestimo, 'form': form})

# UF Views
def uf_list(request):
    ufs = UF.objects.all()
    return render(request, 'uf.html', {'ufs': ufs})

def uf_detail(request, id):
    uf = get_object_or_404(UF, id=id)
    if request.method == 'POST':
        form = UFForm(request.POST, instance=uf)
        if form.is_valid():
            form.save()
            return redirect('uf_list')
    else:
        form = UFForm(instance=uf)
    return render(request, 'uf.html', {'uf': uf, 'form': form})

# Cidade Views
def cidade_list(request):
    cidades = Cidade.objects.all()
    return render(request, 'cidade.html', {'cidades': cidades})

def cidade_detail(request, id):
    cidade = get_object_or_404(Cidade, id=id)
    if request.method == 'POST':
        form = CidadeForm(request.POST, instance=cidade)
        if form.is_valid():
            form.save()
            return redirect('cidade_list')
    else:
        form = CidadeForm(instance=cidade)
    return render(request, 'cidade.html', {'cidade': cidade, 'form': form})

# Usuário Views
def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario.html', {'usuarios': usuarios})

def usuario_detail(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuario.html', {'usuario': usuario, 'form': form})
