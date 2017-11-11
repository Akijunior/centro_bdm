# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-11 05:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('cod_participante', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(default='Nome da Pessoa', max_length=60)),
                ('email', models.CharField(default='pessoa@email.com', max_length=60)),
            ],
        ),
    ]
