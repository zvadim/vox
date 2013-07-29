from django import template

from ..models import Publication

register = template.Library()

@register.assignment_tag
def get_publication(member, num=3, interview=False):
    if interview:
        return member.get_interview[:3]
    return member.get_articles[:3]