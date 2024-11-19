from django.contrib import admin
from .models import *


class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 1


class UFAdmin(admin.ModelAdmin):
    list_display = ('sigla',)
    search_fields = ('sigla',)
    inlines = [CidadeInline]  # Relaciona UF com cidades


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    search_fields = ('nome', 'cidade__nome')

class LivroInline(admin.TabularInline):
    model = Livro
    extra = 1


class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [LivroInline]  # Relaciona Genero com os livros


class LivroInline(admin.TabularInline):
    model = Livro
    extra = 1

class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    search_fields = ('nome', 'cidade__nome')
    inlines = [LivroInline]  # Relaciona Editora com os livros
    


class LivroInline(admin.TabularInline):
    model = Livro  # Relaciona Livro com Autores (muitos para muitos)
    extra = 1


class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    search_fields = ('nome', 'cidade__nome')
    inlines = [LivroInline]  # Relaciona Autor com os livros


class LivroAdmin(admin.ModelAdmin):
    list_display = ( 'editora', 'genero')
    search_fields = ('titulo', 'editora__nome', 'genero__nome')

class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'livro', 'data_emprestimo', 'data_devolucao')
    search_fields = ('usuario__nome', 'livro__titulo')
    list_filter = ('data_emprestimo', 'data_devolucao')  # Filtros por data

admin.site.register(UF, UFAdmin)
admin.site.register(Cidade)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Editora, EditoraAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Livro, LivroAdmin)
admin.site.register(Emprestimo, EmprestimoAdmin)
