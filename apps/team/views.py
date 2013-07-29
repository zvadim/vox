# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render
from . import models as _m


def get_member(request, pk):
    try:
        context = {
            'member': _m.Member.objects.get(pk=pk, is_active=True)
        }
    except _m.Member.DoesNotExist:
        return Http404

    return render(request, 'team/member_block.html', context)