from django import template

from ..models import Publication

register = template.Library()


@register.inclusion_tag('news/tag/block_events.html')
def block_events(num=3):
    return {
        'objects': Publication.objects.event_list()[:num]
    }


@register.inclusion_tag('news/tag/block_news.html')
def block_news(num=5):
    return {
        'objects': Publication.objects.news_list()[:num]
    }


@register.assignment_tag
def get_vacancy_list():
    return Publication.objects.filter(category=Publication.C_VACANCY)
