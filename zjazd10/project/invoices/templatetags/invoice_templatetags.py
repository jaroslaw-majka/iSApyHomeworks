from django import template
from datetime import date

register = template.Library()


@register.filter
def row_styler(payment_date):
    today = date.today()
    if (payment_date - today).days > 7:
        return 'due'
