# -*- coding: utf-8 -*-
from django.db import models


class Page(models.Model):
    C_PR, C_IND, C_PAGE = range(3)
    CATS = (
        (C_PR, u'Практика'),
        (C_IND, u'Индустрия'),
        (C_PAGE, u'Без категории')
    )

    title = models.CharField(u'Заголовок страницы', max_length=128)
    text = models.TextField(u'Текст страницы')
    slug = models.SlugField()
    category = models.CharField(u'Категория', max_length=1, default=C_PAGE, choices=CATS)
    is_active = models.BooleanField(u'Показывать на сайте', default=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Страница'
        verbose_name_plural = u'Страницы'