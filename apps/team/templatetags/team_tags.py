from django import template
from ..models import Publication

register = template.Library()


@register.assignment_tag
def get_publication(member, num=3):
    return member.get_articles[:3]


@register.inclusion_tag('team/tag/block_publ.html')
def block_publication(num=5):
    return {
        'objects': Publication.objects.filter(is_active=True, author__is_active=True)[:num]
    }

@register.inclusion_tag('team/tag/block_interview.html')
def block_publication_random(num=5):
    return {
        'objects': Publication.objects.filter(is_active=True, author__is_active=True).order_by('?')[:num]
    }