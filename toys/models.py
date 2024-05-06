from django.db import models

# Create your models here.
class Toy(models.Model):
    criado = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=150, blank=False, default='')
    descricao = models.CharField(max_length=250, blank=True, default='')
    categoria = models.CharField(max_length=200, blank=False, default='')
    lancamento = models.DateTimeField()
    foi_vendido = models.BooleanField(default=False)

class Meta:
    ordering = ('nome',)