from django.shortcuts import render
from rest_framework import generics
from restaurante.models import Prato
from restaurante.serializers import PratoSerializer

# Create your views here.

class PratoListView(generics.ListAPIView):
  queryset = Prato.objects.all()
  serializer_class = PratoSerializer