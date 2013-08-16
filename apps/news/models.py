# -*- coding: utf-8 -*-
import datetime
from django.contrib.contenttypes.generic import GenericRelation
from django.db import models
from advanced_imagefield.models import AdvancedImage
from django.utils.translation import ugettext as _

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


class Publication(models.Model):
    C_NEWS, C_EVENT, C_VACANCY = xrange(3)
    CATS = (
        (C_NEWS, _(u'Новости')),
        (C_EVENT, _(u'События')),
        (C_VACANCY, _(u'Вакансии'))
    )

    title = models.CharField(u'Заголовок статьи', max_length=128)
    short_text = models.TextField(u'Анонс')
    text = models.TextField(u'Текст публикации')
    create_date = models.DateTimeField(u'Дата создания', default=datetime.datetime.now())
    image = models.ImageField(u'Изображение', upload_to='publication', help_text=u'Точный размер - 600 на 400 px', null=True, blank=True)
    slug = models.SlugField()
    category = models.IntegerField(u'Категория', max_length=1, default=C_NEWS, choices=CATS)
    is_active = models.BooleanField(u'Показывать на сайте', default=True)
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