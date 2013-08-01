# -*- coding: utf-8 -*-
from django.db import models


class Page(models.Model):
    C_PR, C_IND, C_PAGE = xrange(3)
    CATS = (
        (C_PR, u'Практика'),
        (C_IND, u'Индустрия'),
        (C_PAGE, u'Без категории')
    )

    title = models.CharField(u'Заголовок страницы', max_length=128)
    text = models.TextField(u'Текст страницы')
    short_text = models.TextField(u'Анонс', help_text=u'не обязательное поле', blank=True)
    slug = models.SlugField()
    category = models.IntegerField(u'Категория', max_length=1, default=C_PAGE, choices=CATS)
    is_active = models.BooleanField(u'Показывать на сайте', default=True)
    image = models.ImageField(u'Фото', help_text=u'Минимальная ширина - 538px. Не обязательное поле', upload_to='page', null=True, blank=True)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return (
            'site_page_%s' % self.category, (), {'slug': self.slug}
        )

    class Meta:
        verbose_name = u'Страница'
        verbose_name_plural = u'Страницы'


class Client(models.Model):
    title = models.CharField(u'Название', max_length=64)
    image = models.ImageField(u'Иконка', help_text=u'Размер - 145 на 140 px', upload_to='clients')
    is_active = models.BooleanField(u'Показывать на сайте', default=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Клиент'
        verbose_name_plural = u'Клиенты'


class ClientQuote(models.Model):
    title = models.CharField(u'Подпись', max_length=64, help_text=u'Запятая заменяется на перевод строки')
    text = models.TextField(u'Цитата')
    is_active = models.BooleanField(u'Показывать на сайте', default=True)

    def __unicode__(self):
        return self.title

    @property
    def title_list(self):
        return self.title.split(',')

    class Meta:
        verbose_name = u'Высказывание клиента'
        verbose_name_plural = u'Высказывания'
