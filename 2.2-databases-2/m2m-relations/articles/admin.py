from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError

from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main') is True:
                count += 1
            if count > 1:
                raise ValidationError('Основным может быть только один тег')
        if count == 0:
            raise ValidationError('Укажите основной тег')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 1
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    list_filter = ['published_at']
    inlines = [ScopeInline,]
    pass


@admin.register(Tag)
class Tag(admin.ModelAdmin):
    list_display = ['id', 'name']
    pass
