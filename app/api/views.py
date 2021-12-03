from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

from core.models import Video

from api import serializers


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class VideoViewSet(generics.ListAPIView):
    """Manage Videos in the database"""
    queryset = Video.objects.all().order_by('-publishing_datetime')
    serializer_class = serializers.VideoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['vid','title']
    ordering_fields = ['vid', 'title']
    search_fields = ['title', 'description']
    pagination_class = StandardResultsSetPagination



