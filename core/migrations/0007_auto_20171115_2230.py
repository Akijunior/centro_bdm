# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-16 01:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20171115_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='imagem_principal',
            field=models.FileField(default='media/logo_centro.png', upload_to='noticias/%Y/%m/%d'),
        ),
    ]
