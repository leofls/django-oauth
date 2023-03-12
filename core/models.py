from django.db import models

# Create your models here.
class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.descricao}"

class Editora(models.Model):
    nome = models.CharField(max_length=50)
    site = models.URLField()

    