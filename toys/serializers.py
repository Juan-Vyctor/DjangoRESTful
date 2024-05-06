from rest_framework import serializers
from toys.models import Toy

class ToySerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=150)
    descricao = serializers.CharField(max_length=250)
    lancamento = serializers.DateTimeField()
    categoria = serializers.CharField(max_length=200)
    foi_vendido = serializers.BooleanField(required=False)

def create(self, validated_data):
    return Toy.objects.create(**validated_data)

def update(self, instance, validated_data):
    instance.nome = validated_data.get('nome', instance.nome)
    instance.descricao = validated_data.get('descricao', instance.descricao)
    instance.lancamento = validated_data.get('lancamento', instance.lancamento)
    instance.categoria = validated_data.get('categoria', instance.categoria)
    instance.foi_vendido = validated_data.get('foi_vendido', instance.foi_vendido)
    instance.save()
    return instance