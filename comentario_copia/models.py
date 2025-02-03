from django.db import models

# Create your models here.
class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    descricao = models.TextField(max_length=255)
    

    def __str__(self):
        return self.nome