from django import template

from ..models import Page, ClientQuote

register = template.Library()

@register.inclusion_tag('tag/top_menu.html')
def top_menu_display():
    return {
        'ind': Page.objects.filter(category=Page.C_IND),
        'prc': Page.objects.filter(category=Page.C_PR)
    }

@register.assignment_tag
def get_page(slug):
    try:
        return Page.objects.get(slug=slug)
    except Page.DoesNotExist:
        return None


@register.inclusion_tag('tag/client_quote.html')
def client_quote():
    return {
        'objects': ClientQuote.objects.filter(is_active=True)
    }