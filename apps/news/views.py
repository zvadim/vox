# -*- coding: utf-8 -*-
from django.views.generic import DetailView, ListView
from . import models as _m
from django.utils.translation import ugettext as _


class GenericPageView(DetailView):
    model = _m.Publication


class GenericListView(ListView):
    model = _m.Publication
    type_id = _m.Publication.C_NEWS
    paginate_by = 10

    def get_context_data(self, **kwargs):
        ret = super(GenericListView, self).get_context_data(**kwargs)
        cats = {}
        for i in _m.Publication.CATS:
            cats.update({i[0]: i[1]})

        ret.update({
            'page_title': cats[self.type_id]
        })
        return ret


    def get_queryset(self):
        return super(GenericListView, self).get_queryset().filter(category=self.type_id)


news_list = GenericListView.as_view()
events_list = GenericListView.as_view(type_id=_m.Publication.C_EVENT)
publication_item = GenericPageView.as_view()

