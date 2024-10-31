# Generated by Django 3.2.25 on 2024-10-03 00:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=100)),
                ('data_publicacao', models.DateTimeField(default=datetime.datetime.now)),
                ('numero_paginas', models.IntegerField()),
            ],
        ),
    ]