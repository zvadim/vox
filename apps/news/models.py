# -*- coding: utf-8 -*-
from django.db import models


class Publication(models.Model):
    C_NEWS, C_EVENT, C_VACANCY = range(3)
    CATS = (
        (C_NEWS, u'Новость'),
        (C_EVENT, u'Событие'),
        (C_VACANCY, u'Вакансия')
    )

    title = models.CharField(u'Заголовок статьи', max_length=128)
    short_text = models.TextField(u'Анонс')
    text = models.TextField(u'Текст публикации')
    create_date = models.DateField(auto_now_add=True)
    image = models.ImageField(u'Изображение', upload_to='publication')
    slug = models.SlugField()
    category = models.CharField(u'Категория', max_length=1, default=C_NEWS, choices=CATS)
    is_active = models.BooleanField(u'Показывать на сайте', default=True)
    is_top = models.BooleanField(u'Показывать в главном слайдере', default=False)
    top_banner = models.ImageField(u'Изображение для топ-слайдера', upload_to='top-banner', help_text=u'ШхВ px')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Материал'
        verbose_name_plural = u'Материалы'