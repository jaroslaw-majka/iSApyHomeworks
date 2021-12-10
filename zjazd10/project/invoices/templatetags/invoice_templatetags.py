from django import template
from datetime import date

register = template.Library()


@register.filter
def row_styler(invoice):
    payment_status = invoice.payment_status
    payment_date = invoice.payment_date
    today = date.today()
    if payment_status:
        return 'paid'
    elif (payment_date - today).days > 7:
        return 'due'
