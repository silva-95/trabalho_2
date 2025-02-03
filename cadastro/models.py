from django.db import models

# Create your models here.
class Pessoa(models.Model):  
    id = models.AutoField(primary_key=True)   
    nome = models.TextField(max_length=100)
    idade = models.TextField(max_length=20)
    email = models.EmailField()
    sexo = models.CharField(null=True, max_length=1)
    # nascimento = models.DateField(null=True)
    telefone = models.TextField(null=True)

    def __str__(self):
        return self.nome