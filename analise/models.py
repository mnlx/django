from django.db import models

# Create your models here.

class Analise(models.Model):
    listas_de_inclusao = models.CharField(null=False, max_length=2000)
    denuncias = models.IntegerField(null=False)
    spf = models.CharField(null=False,max_length=30)
    erros_permanentes = models.CharField(null=False,max_length=200)
    media_clicks_3_meses = models.CharField(null=False,max_length=10)
    dominio_proprio = models.CharField(null=False,max_length=30)
    nunca_interagiram = models.IntegerField(null=False)
    contatos_base = models.IntegerField(null=False)
    analise = models.DateTimeField(null=False)
    html = models.CharField(null=False, max_length=10000)
    campanha = models.CharField(null=False,max_length=200)
    interacao_12_meses = models.IntegerField(null=False)
    media_visualizacao_3_meses = models.CharField(null=False,max_length=10)
    listas_de_exclusao = models.CharField(null=False,max_length=200)
    campanhas_interrompidas_no_mes = models.IntegerField(null=False)
    interacao_6_meses = models.IntegerField(null=False)
    cancelamentos = models.IntegerField(null=False)
    dkim=models.CharField(null=False,max_length=30)
    segmentacao= models.CharField(null=False,max_length=200)
    qualidade_de_base= models.CharField(null=False,max_length=3)
