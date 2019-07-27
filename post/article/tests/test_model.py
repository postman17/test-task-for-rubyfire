import datetime

from django.test import TestCase
from django.utils import timezone
from psycopg2.extras import DateTimeTZRange

from ..models import Article


class ArticleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Article.objects.create(
            title='Test article',
            text='text for test article',
            likes=5,
            dislikes=2,
            active_range=DateTimeTZRange(
                timezone.now() - datetime.timedelta(days=1),
                timezone.now() + datetime.timedelta(days=1),
            )
        )

    def test_title_label(self):
        article = Article.objects.get(id=1)
        field_label = article._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Заголовок')

    def test_title_max_length(self):
        article = Article.objects.get(id=1)
        max_length = article._meta.get_field('title').max_length
        self.assertEquals(max_length, 255)

    def test_text_label(self):
        article = Article.objects.get(id=1)
        field_label = article._meta.get_field('text').verbose_name
        self.assertEquals(field_label, 'Текст')

    def test_likes_label(self):
        article = Article.objects.get(id=1)
        field_label = article._meta.get_field('likes').verbose_name
        self.assertEquals(field_label, 'Лайки')

    def test_dislikes_label(self):
        article = Article.objects.get(id=1)
        field_label = article._meta.get_field('dislikes').verbose_name
        self.assertEquals(field_label, 'Дизлайки')

    def test_version_label(self):
        article = Article.objects.get(id=1)
        field_label = article._meta.get_field('active_range').verbose_name
        self.assertEquals(field_label, 'Active range')

    def test_object_name(self):
        article = Article.objects.get(id=1)
        expected_object_name = str(article.title)
        self.assertEquals(expected_object_name, str(article))
