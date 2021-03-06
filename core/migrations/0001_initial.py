# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-08 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('cod_noticia', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(default='Titulo noticia', max_length=60, unique=True)),
                ('autor', models.CharField(default='Autor noticia', max_length=60)),
                ('texto', models.CharField(default='Autor texto', max_length=2000)),
                ('categoria', models.CharField(default='Espiritismo', max_length=40)),
                ('data', models.DateField(null=True)),
                ('hora', models.TimeField(null=True)),
                ('acessos', models.IntegerField(default=0)),
            ],
        ),
    ]
