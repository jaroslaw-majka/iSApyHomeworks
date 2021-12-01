from django.shortcuts import render
from django.views.generic import ListView
from invoices.models import Invoice


class InvoiceListView(ListView):
    model = Invoice
    template = 'invoice_list.html'
