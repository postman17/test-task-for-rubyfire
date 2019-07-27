from django import forms
from django.contrib import admin
from django.contrib.admin import widgets
from django.contrib.postgres.forms import RangeWidget

from .models import Article


class CustomWidget(widgets.AdminSplitDateTime):
    def value_from_datadict(self, data, files, name):
        temp = [widget.value_from_datadict(data, files, name + '_%s' % i) for i, widget in enumerate(self.widgets)]
        return ' '.join(temp)


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        widgets = {
            'active_range': RangeWidget(CustomWidget)
        }
        fields = '__all__'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    list_display = ('title', 'likes', 'dislikes', 'final_sum')

    def final_sum(self, obj):
        return obj.likes - obj.dislikes

    final_sum.short_description = 'Итоговая сумма'
