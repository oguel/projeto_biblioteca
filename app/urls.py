from django.urls import path
from . import views

urlpatterns = [
    # Index/Home
    path('', views.index, name='index'),

    # Livro
    path('livros/', views.livro_list, name='livro_list'),
    path('livros/<int:id>/', views.livro_detail, name='livro_detail'),

    # Gênero
    path('generos/', views.genero_list, name='genero_list'),
    path('generos/<int:id>/', views.genero_detail, name='genero_detail'),

    # Editora
    path('editoras/', views.editora_list, name='editora_list'),
    path('editoras/<int:id>/', views.editora_detail, name='editora_detail'),

    # Autor
    path('autores/', views.autor_list, name='autor_list'),
    path('autores/<int:id>/', views.autor_detail, name='autor_detail'),

    # Empréstimo
    path('emprestimos/', views.emprestimo_list, name='emprestimo_list'),
    path('emprestimos/<int:id>/', views.emprestimo_detail, name='emprestimo_detail'),

    # UF
    path('ufs/', views.uf_list, name='uf_list'),
    path('ufs/<int:id>/', views.uf_detail, name='uf_detail'),

    # Cidade
    path('Cidades/', views.cidade_list, name='cidade_list'),
    path('Cidades/<int:id>/', views.cidade_detail, name='cidade_detail'),

    # Usuário
    path('usuarios/', views.usuario_list, name='usuario_list'),
    path('usuarios/<int:id>/', views.usuario_detail, name='usuario_detail'),
]
