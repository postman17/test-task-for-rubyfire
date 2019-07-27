from django.urls import path

from .viewsets import ArticleListView


urlpatterns = [
    path('search/', ArticleListView.as_view()),

]
