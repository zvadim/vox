from django import template

from ..models import Page

register = template.Library()

@register.inclusion_tag('tag/top_menu.html')
def top_menu_display():
    return {
        'ind': Page.objects.filter(category=Page.C_IND),
        'prc': Page.objects.filter(category=Page.C_PR)
    }