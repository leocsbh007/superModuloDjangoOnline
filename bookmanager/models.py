from django.db import models
from datetime import datetime

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    data_publicacao = models.DateTimeField(default=datetime.now, blank=False)
    numero_paginas = models.IntegerField()

    def __str__(self):
        return self.titulo
