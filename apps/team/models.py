# -*- coding: utf-8 -*-
from django.db import models


class Team(models.Model):
    name = models.CharField(u'ФИО', max_length=64)
    position = models.CharField(u'Должность', max_length=64)
    email = models.EmailField()
    about = models.TextField(u'Инфо')

    def __unicode__(self):
        return self.name


class Publication(models.Model):
    author = models.ForeignKey('Team')
    title = models.CharField(u'Заголовок статьи', max_length=128)
    text = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    image = models.ImageField(u'Изображение', upload_to='publication')

    def __unicode__(self):
        return self.title

