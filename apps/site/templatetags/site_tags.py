from django import template
from django.core.urlresolvers import reverse
from django.utils import translation

from ..models import Page, ClientQuote, TopSlider
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


@register.inclusion_tag('site/tag/top_slider.html')
def top_slider_display():
    cur_language = translation.get_language()
    return {
        'slides': TopSlider.objects.filter(is_active=True, language=cur_language).order_by('?')
    }

@register.simple_tag
def get_i18n_page_url(request, language):
    cur_language = translation.get_language()

    try:
        translation.activate(language)
        url = reverse(request.resolver_match.url_name, kwargs=request.resolver_match.kwargs)
    except Exception, e:
        url = ''
    finally:
        translation.activate(cur_language)
    return url