from django.shortcuts import render
from rest_framework import viewsets
from .models import Consumer
from .serializers import ConsumerSerializer

class ConsumerViewSet(viewsets.ModelViewSet):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer