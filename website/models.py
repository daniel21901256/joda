from django.db import models


# Create your models here.

class contacto(models.Model):
    nome = models.CharField(max_length=20)
    apelido = models.CharField(max_length=20)
    telefone = models.IntegerField()
    email = models.EmailField(max_length=64)
    dataNasc = models.DateField()

    def __str__(self):
        return f"{self.nome} {self.apelido}"


class quizz(models.Model):
    pergunta_1 = models.CharField(max_length=2)
    pergunta_2 = models.CharField(max_length=2)
    pergunta_3 = models.CharField(max_length=2)
    pergunta_4 = models.CharField(max_length=2)
    pergunta_5 = models.CharField(max_length=15)
    pergunta_6 = models.CharField(max_length=15)
    pergunta_7 = models.CharField(max_length=15)
    pergunta_8 = models.CharField(max_length=2)
    pergunta_9 = models.CharField(max_length=2)
    pergunta_10 = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.pergunta_1},{self.pergunta_2},{self.pergunta_4}" \
               f",{self.pergunta_5},{self.pergunta_6},{self.pergunta_7},{self.pergunta_8}" \
               f",{self.pergunta_9},{self.pergunta_10}"


class Post(models.Model):
    avaliacao = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.avaliacao}"
