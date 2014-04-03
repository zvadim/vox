# -*- coding: utf-8 -*-
from django.views.generic import DetailView, ListView
from . import models as _m
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _


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


class FeedView(Feed):
    title = ''
    link = ''
    type_id = _m.Publication.C_NEWS

    def __call__(self, request, *args, **kwargs):
        self.link = reverse_lazy('news_list')
        self.title = _(u'Новости')

        return super(FeedView, self).__call__(request, *args, **kwargs)

    def items(self):
        return _m.Publication.objects.filter(category=self.type_id)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.short_text


class EventFeedView(FeedView):
    type = _m.Publication.C_EVENT

news_list = GenericListView.as_view()
news_feed = FeedView()
events_list = GenericListView.as_view(type_id=_m.Publication.C_EVENT)
events_feed = EventFeedView()
publication_item = GenericPageView.as_view()

