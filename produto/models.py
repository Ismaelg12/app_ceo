from django.db import models
from django.urls import reverse_lazy
import datetime
from django.utils import timezone


class Produto(models.Model):
    produto        = models.CharField(max_length=100, unique=True)
    estoque        = models.IntegerField('estoque atual')
    estoque_minimo = models.PositiveIntegerField('estoque mínimo', default=0)
    validade       = models.DateField(null=True, blank=True)
    categoria      = models.ForeignKey(
        'Categoria',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('produto',)

    def __str__(self):
        return self.produto

    def get_absolute_url(self):
        return reverse_lazy('produto_detail', kwargs={'pk': self.pk})

    def to_dict_json(self):
        return {
            'pk': self.pk,
            'produto': self.produto,
            'estoque': self.estoque,
        }

    @property
    def verifica_vencimento(self):
        data_atual      = datetime.date.today()
        futuro          = self.validade - datetime.timedelta(days=7)

        if data_atual >= self.validade:
            return "Vencido"
        elif data_atual > futuro and data_atual < self.validade:
            return "Alerta"
        else:
            return "Valido"    

class Categoria(models.Model):
    categoria = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('categoria',)

    def __str__(self):
        return self.categoria
