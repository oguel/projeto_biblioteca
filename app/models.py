from django.db import models

class UF(models.Model):
    sigla = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.sigla

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.ForeignKey(UF, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.uf}"
    
class Pessoa(models.Model):
        nome = models.CharField(max_length=100, default='')
        email = models.CharField(max_length=100, default='')
        cidade = models.ForeignKey(Cidade,on_delete=models.CASCADE, null=True, blank=True)
        telefone = models.IntegerField(default=0)

        class Meta:
            abstract = True
        def __str__(self):
            return self.nome
    

class Usuario(Pessoa):
    pass

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        

class Genero(models.Model):
    nome = models.CharField(max_length=100, unique=True)

# Superclass de 'Pessoa' que sera uma classe pai para: PessoaFisica e Pessoa Juridica
class PessoaFisica(Pessoa):
        cpf = models.IntegerField(default=0)
        data_nasc = models.DateField(default='2000-01-01',verbose_name='Data de Nascimento')
        

        class Meta:
           abstract = True
        
        def __str__(self): 
            return self.nome
   
class PessoaJuridica(Pessoa):
        cnpj = models.IntegerField(default=0)
        razao_social = models.CharField(max_length=100, default='')
        data_fundacao = models.DateField(default='2000-01-01',verbose_name='Data de Nascimento')

        class Meta:
         abstract = True

         def __str__(self): 
            return self.nome
    
class Editora(PessoaJuridica):
    site = models.CharField()

    class Meta:
        verbose_name = "Editora"
        verbose_name_plural = "Editoras"


class Autor(PessoaFisica):

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.nome


class Livro(models.Model):
    nome = models.CharField(max_length=200)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data_publicacao = models.DateField(default='2000-01-01')

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    data_emprestimo = models.DateField(default='2000-01-01')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_devolucao = models.DateField(default='2000-01-01')

    def __str__(self):
        return f"Empréstimo de {self.livro} para {self.usuario} em {self.data_emprestimo}"
