import datetime

from django.utils import timezone
from rest_framework import generics
from rest_framework import filters
from psycopg2.extras import DateTimeTZRange

from .serializer import ArticleSerializer
from .models import Article


class ArticleFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(active_range__overlap=DateTimeTZRange(
            timezone.now() - datetime.timedelta(hours=1),
            timezone.now() + datetime.timedelta(hours=1),
        ))


class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [ArticleFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'text']
