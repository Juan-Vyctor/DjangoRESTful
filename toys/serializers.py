from rest_framework import serializers
from toys.models import Toy

class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = ('id',
        'nome',
        'descricao',
        'lancamento',
        'categoria',
        'foi_vendido')