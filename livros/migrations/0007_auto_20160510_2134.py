# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-11 00:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0006_auto_20160508_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimolivro',
            name='escola',
            field=models.CharField(default='IFRN-JC', max_length=40, verbose_name='Escola'),
        ),
        migrations.AlterField(
            model_name='emprestimolivro',
            name='nome',
            field=models.CharField(default='nomeAluno', max_length=40, verbose_name='Nome'),
        ),
    ]
