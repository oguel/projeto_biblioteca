# Generated by Django 5.1.2 on 2024-11-12 18:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_editora_cidade_editora_email_editora_nome_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name': 'Usuário', 'verbose_name_plural': 'Usuários'},
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='data_nasc',
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_devolucao',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='data_publicacao',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.cidade'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefone',
            field=models.IntegerField(default=0),
        ),
    ]
