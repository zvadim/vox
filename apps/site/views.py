# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, FormView
from . import models as _m

class MainPageView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        ret = super(MainPageView, self).get_context_data(**kwargs)
        ret['clients'] = _m.Client.objects.filter(is_active=True)
        return ret

main = MainPageView.as_view()