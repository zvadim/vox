# -*- coding: utf-8 -*-
from django.db import models


class Member(models.Model):
    name = models.CharField(u'ФИО', max_length=64)
    slug = models.SlugField()
    position = models.CharField(u'Должность', max_length=64)
    email = models.EmailField()
    tel = models.CharField(u'Телефоны', max_length=255, help_text=u'Пробел заменяется на перевод строки')
    about = models.TextField(u'Инфо')
    is_active = models.BooleanField(u'Показывать на сайте', default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Член команды'
        verbose_name_plural = u'Команда'


class Publication(models.Model):
    author = models.ForeignKey('Member')
    category = models.ForeignKey('Category')
    title = models.CharField(u'Заголовок статьи', max_length=128)
    short_text = models.TextField(u'Анонс')
    text = models.TextField(u'Текст публикации')
    create_date = models.DateField(auto_now_add=True)
    image = models.ImageField(u'Изображение', upload_to='publication')
    slug = models.SlugField()
    is_active = models.BooleanField(u'Показывать на сайте', default=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Публикация'
        verbose_name_plural = u'Публикации'


class Category(models.Model):
    title = models.CharField(u'Название категории', max_length=64)
    slug = models.SlugField()
    is_interview = models.BooleanField(u'Это интервью', default=False, help_text=u'Отметить если в этой категории публикуются только интервью')
    is_active = models.BooleanField(u'Показывать на сайте', default=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'

