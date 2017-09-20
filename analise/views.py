from django.shortcuts import render
from rest_framework import generics,response
from .models import Analise
from .serializers import AnaliseSerializer

Response = response.Response
# Create your views here.
#
# class AnaliseList(generics.ListCreateAPIView):
#     queryset = Analise.objects.all()
#     serializer_class = AnaliseSerializer
#
from rest_framework import viewsets,renderers

from rest_framework.decorators import detail_route

class AnaliseViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Analise.objects.all()
    serializer_class = AnaliseSerializer


    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def analise_html(self, request, *args, **kwargs):
        analise_html = self.get_object()
        return Response(analise_html.html)

