# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render
from . import models as _m
from django.views.generic import DetailView


def get_member(request, pk):
    try:
        context = {
            'member': _m.Member.objects.get(pk=pk, is_active=True)
        }
    except _m.Member.DoesNotExist:
        print 'fail'
        return Http404

    return render(request, 'team/member_block.html', context)


class GenericPageView(DetailView):
    model = _m.Publication


generic_page = GenericPageView.as_view()