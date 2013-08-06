# -*- coding: utf-8 -*-
import datetime
from django.contrib.contenttypes.generic import GenericRelation
from django.db import models
from advanced_imagefield.models import AdvancedImage


class CustomManager(models.Manager):
    def news_list(self, **kwargs):
        kwargs['category'] = Publication.C_NEWS
        kwargs['is_active'] = True
        return super(CustomManager, self).get_query_set().filter(**kwargs)

    def event_list(self, **kwargs):
        kwargs['category'] = Publication.C_EVENT
        kwargs['is_active'] = True
        return super(CustomManager, self).get_query_set().filter(**kwargs)

    def vacancy_list(self, **kwargs):
        kwargs['category'] = Publication.C_VACANCY
        kwargs['is_active'] = True
        return super(CustomManager, self).get_query_set().filter(**kwargs)

    def slide_list(self, **kwargs):
        kwargs['category'] = Publication.C_NEWS
        kwargs['is_active'] = True
        kwargs['is_top'] = True
        kwargs['top_banner__isnull'] = False
        return super(CustomManager, self).get_query_set().filter(**kwargs)


class Publication(models.Model):
    C_NEWS, C_EVENT, C_VACANCY = xrange(3)
    CATS = (
        (C_NEWS, u'Новость'),
        (C_EVENT, u'Событие'),
        (C_VACANCY, u'Вакансия')
    )

    title = models.CharField(u'Заголовок статьи', max_length=128)
    short_text = models.TextField(u'Анонс')
    text = models.TextField(u'Текст публикации')
    create_date = models.DateTimeField(u'Дата создания', default=datetime.datetime.now())
    image = models.ImageField(u'Изображение', upload_to='publication')
    slug = models.SlugField()
    category = models.IntegerField(u'Категория', max_length=1, default=C_NEWS, choices=CATS)
    is_active = models.BooleanField(u'Показывать на сайте', default=True)
    is_top = models.BooleanField(u'Показывать в главном слайдере', default=False, help_text=u'Обязательно нужно добавить изображение для ТОП-слайдера')
    top_banner = models.ImageField(u'Изображение для топ-слайдера', upload_to='top-banner', help_text=u'Размер - 1136 на 484 px', null=True, blank=True)
    gallery = GenericRelation(AdvancedImage)

    objects = CustomManager()

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return (
            'news_publication_item', (), {'slug': self.slug, 'type': ['news', 'event', 'vacancy'][self.category]}
        )

    class Meta:
        verbose_name = u'Материал'
        verbose_name_plural = u'Материалы'
        ordering = ['-create_date', '-pk']