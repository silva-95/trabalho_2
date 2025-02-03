from django.db import models

# Create your models here.
class Endereco(models.Model):
    rua = models.TextField(max_length=100)
    bairro = models.TextField(max_length=100)
    cidade = models.TextField(max_length=100)
    estado = models.TextField(max_length=100)
    pais = models.TextField(max_length=100)

   