from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def row_styler(invoice):
    style = 'color: red'
    return mark_safe(style)
