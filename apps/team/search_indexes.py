# -*- coding: utf-8 -*-
import datetime
from haystack import indexes
from .models import Publication


class PublicationIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    create_date = indexes.DateTimeField(model_attr='create_date')

    def get_model(self):
        return Publication

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(create_date__lte=datetime.datetime.now())