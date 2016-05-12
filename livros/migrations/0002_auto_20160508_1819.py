# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-08 21:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmprestimoLivro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produtosanterior', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Quantidade de Produtos anterior')),
                ('quantidade', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Quantidade')),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='T\xedtulo')),
                ('numero', models.DecimalField(decimal_places=10, default=0, max_digits=15, verbose_name='N\xfamero do livro')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='livro/')),
            ],
        ),
        migrations.RemoveField(
            model_name='incluirfornecedor',
            name='fornecedor',
        ),
        migrations.DeleteModel(
            name='Fornecedor',
        ),
        migrations.DeleteModel(
            name='IncluirFornecedor',
        ),
        migrations.AddField(
            model_name='emprestimolivro',
            name='livro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livros.Livro'),
        ),
    ]
