# Generated by Django 2.2.3 on 2019-07-26 11:07

import django.contrib.postgres.fields.ranges
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('likes', models.PositiveIntegerField(verbose_name='Лайки')),
                ('dislikes', models.PositiveIntegerField(verbose_name='Дизлайки')),
                ('active_range', django.contrib.postgres.fields.ranges.DateTimeRangeField(verbose_name='Active range')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.AddIndex(
            model_name='article',
            index=models.Index(fields=['title', 'text', 'active_range'], name='article_art_title_0196e0_idx'),
        ),
    ]
