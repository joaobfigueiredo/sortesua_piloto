from django.db import models

class Aposta(models.Model):
    ponto_de_venda = models.CharField(max_length=75)
    contato = models.CharField(max_length=20)
    apostador = models.CharField(max_length=75)
    numeros = models.CharField(max_length=40)
    validacao = models.DateTimeField(auto_now=True)