# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, DetailView
from . import models as _m
from apps.team import models as _mt


class MainPageView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        ret = super(MainPageView, self).get_context_data(**kwargs)
        ret.update({
            'clients': _m.Client.objects.filter(is_active=True),
            'members': _mt.Member.objects.filter(is_active=True)
        })

        return ret


class GenericPageView(DetailView):
    model = _m.Page


main = MainPageView.as_view()
generic_page = GenericPageView.as_view()