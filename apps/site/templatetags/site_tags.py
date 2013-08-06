from django import template

from ..models import Page, ClientQuote
from apps.team.models import Category

register = template.Library()

@register.inclusion_tag('site/tag/top_menu.html')
def top_menu_display():
    return {
        'ind': Page.objects.filter(category=Page.C_IND),
        'prc': Page.objects.filter(category=Page.C_PR),
        'cats': Category.objects.filter(is_active=True)
    }

@register.assignment_tag
def get_page(slug):
    try:
        return Page.objects.get(slug=slug)
    except Page.DoesNotExist:
        return None


@register.inclusion_tag('site/tag/client_quote.html')
def client_quote():
    return {
        'objects': ClientQuote.objects.filter(is_active=True)
    }