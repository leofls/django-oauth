from django.shortcuts import render
from core.models import Categoria, Editora

from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasReadWriteScope
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from django_filters import rest_framework as filters
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated, AllowAny


class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'descricao']

class CertidaoFilter(filters.FilterSet):
    descricao_categoria = filters.CharFilter(field_name="descricao", lookup_expr="in")
    class Meta:
        model = Categoria
        fields = ["descricao"]


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [ IsAuthenticated]
    filterset_class = CertidaoFilter
    filter_fields = {
        'modalidade_certidao': ["in", "exact"], 
    }
    

