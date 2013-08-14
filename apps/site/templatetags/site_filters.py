from django import template

register = template.Library()


@register.filter(name='get_roman_month')
def roman_month(month):
    m = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
    return m[int(month)-1]

@register.filter(name='nl_comma')
def nl_comma(string):
    return '<br>'.join(string.split(','))