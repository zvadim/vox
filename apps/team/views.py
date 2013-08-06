# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from . import models as _m
from django.views.generic import DetailView, ListView


def get_member(request, pk):
    try:
        context = {
            'member': _m.Member.objects.get(pk=pk, is_active=True)
        }
    except _m.Member.DoesNotExist:
        return Http404
    return render(request, 'team/member_block.html', context)


class GenericPageView(DetailView):
    model = _m.Publication

generic_page = GenericPageView.as_view()


class GenericListView(ListView):
    model = _m.Publication
    category = None
    paginate_by = 10

    def dispatch(self, request, *args, **kwargs):
        if 'slug' in kwargs:
            self.category = get_object_or_404(_m.Category, slug=kwargs['slug'])

        return super(GenericListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ret = super(GenericListView, self).get_context_data(**kwargs)
        ret.update({
            'category': self.category,
            'page_title': self.category.title if self.category else None
        })
        return ret

    def get_queryset(self):
        qs = super(GenericListView, self).get_queryset()
        if self.category:
            qs = qs.filter(category=self.category)
        return qs


publication_list = GenericListView.as_view()