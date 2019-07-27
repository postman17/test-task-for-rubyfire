from django.db import models
from django.contrib.postgres.fields import DateTimeRangeField


class Article(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Текст')
    likes = models.PositiveIntegerField('Лайки')
    dislikes = models.PositiveIntegerField('Дизлайки')
    active_range = DateTimeRangeField('Active range')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        indexes = [
            models.Index(fields=['title', 'text', 'active_range']),
        ]
