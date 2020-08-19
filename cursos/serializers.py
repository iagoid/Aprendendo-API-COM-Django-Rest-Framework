from rest_framework import serializers
from django.db.models import Avg

from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        # Não mostra o email quando alguém buscar as informações
        extra_kwargs = {
            'email': {'write_only': True}
        }
        # Qual model eu quero usar
        model = Avaliacao
        # Quais campos eu que mostrar
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo',
        )

    def validate_avaliacao(self, valor):
        if valor in range(1, 6):
            return valor
        raise serializers.ValidationError('A avaliação precisa ser um número entre 1 e 5')



class CursoSerializer(serializers.ModelSerializer):
    # Nested Relationship
    # avaliacoes =AvaliacaoSerializer(many=True, read_only=True)

    #Hyperlinked Related Field
    # avaliacoes = serializers.HyperlinkedRelatedField(
        # many=True, read_only=True, view_name="avaliacao-detail")

    # Primary Key Related Field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    media_avaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes'
        )

    def get_media_avaliacoes(self, obj):
        # pega as avaliacoes faz a media com cada uma das avaliaco e pega eles pelo avaliacao__avg
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')
        if media is None:
            return 0
        # Apenas arredonda a media
        return round(media * 2 ) / 2

