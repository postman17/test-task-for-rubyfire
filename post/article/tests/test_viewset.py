import datetime
import json

from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from django.utils import timezone
from psycopg2.extras import DateTimeTZRange

from ..viewsets import ArticleListView
from ..models import Article


class ArticleListViewTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.test_time = DateTimeTZRange(
                timezone.now() - datetime.timedelta(days=1),
                timezone.now() + datetime.timedelta(days=1),)
        Article.objects.create(
            title='Test article',
            text='text for test article',
            likes=5,
            dislikes=2,
            active_range=self.test_time
        )
        Article.objects.create(
            title='article',
            text='text for article',
            likes=7,
            dislikes=3,
            active_range=self.test_time
        )
        Article.objects.create(
            title='test article 2',
            text='text for article',
            likes=7,
            dislikes=3,
            active_range=DateTimeTZRange(
                timezone.now() - datetime.timedelta(days=5),
                timezone.now() - datetime.timedelta(days=2),)
        )

    def test_article_viewset(self):
        request = self.factory.get('search/?query=test')
        view = ArticleListView.as_view()
        response = view(request)
        response.render()
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[0]['title'], 'Test article')
