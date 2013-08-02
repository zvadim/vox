# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, DetailView
from . import models as _m

def news_list(request):
    pass

def publication_list(request):
    pass


class GenericPageView(DetailView):
    model = _m.Publication


publication_item = GenericPageView.as_view()