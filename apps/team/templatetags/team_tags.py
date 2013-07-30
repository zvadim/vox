from django import template

from ..models import Publication

register = template.Library()

@register.assignment_tag
def get_publication(member, num=3, interview=False):
    if interview:
        return member.get_interview[:3]
    return member.get_articles[:3]

@register.inclusion_tag('team/tag/block_publ.html')
def block_publication(num=5):
    return {
        'objects': Publication.objects.filter(category__is_interview=False)[:num]
    }


@register.inclusion_tag('team/tag/block_interview.html')
def block_interview(num=3):
    return {
        'objects': Publication.objects.filter(category__is_interview=True)[:num]
    }