from django.shortcuts import render
from django.views.generic import ListView

from invoices.models import Invoice


class InvoiceListView(ListView):
    model = Invoice
    template = 'invoice_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        return context
