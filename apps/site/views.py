# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, FormView


class MainPageView(TemplateView):
    template_name = 'base.html'

main = MainPageView.as_view()