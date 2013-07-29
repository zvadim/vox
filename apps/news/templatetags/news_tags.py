from django import template

from ..models import Publication

register = template.Library()

@register.inclusion_tag('tag/top_slider.html')
def top_slider_display():
    return {
        'slides': Publication.objects.slide_list()[:5]
    }