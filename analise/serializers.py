from rest_framework import serializers
from .models import Analise

class AnaliseSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='analise:analise-detail',
        lookup_field='pk'
    )

    html = serializers.HyperlinkedIdentityField(
        view_name='analise:html-detail',
        lookup_field='pk'
    )
    class Meta:
        model = Analise
        fields = ('url','denuncias', 'spf', 'interacao_6_meses',
                  'dominio_proprio', 'campanha', 'html',
                  'analise', 'qualidade_de_base', 'listas_de_inclusao',
                  'nunca_interagiram', 'campanhas_interrompidas_no_mes',
                  'cancelamentos', 'contatos_base', 'erros_permanentes',
                  'media_visualizacao_3_meses', 'interacao_12_meses',
                  'media_clicks_3_meses', 'dkim', 'listas_de_exclusao', 'segmentacao')