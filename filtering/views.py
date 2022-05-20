from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import introduction
from .serializers import introductionserializer

# Introduction viewset
class IntroductionViewSet(ModelViewSet):                 #used modelviewset
    queryset = introduction.objects.all()
    serializer_class = introductionserializer
    print(queryset)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'name']
    search_fields = ['=name', 'intro']
    ordering_fields = ['name', 'id']
    ordering = ['id']

