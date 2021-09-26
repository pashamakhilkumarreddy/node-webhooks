from django import forms
from django.shortcuts import render
from django.views.generic import ListView, DetailView
import pandas as pd
from .models import Sale
from .forms import SalesSearchForm

# Create your views here.

def home_view(request):
    form = SalesSearchForm(request.POST or None)

    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')

        qs = Sale.objects.all()

    context = {
        'form': form
    }
    return render(request, 'sales/home.html', context)


class SaleListView(ListView):
    model = Sale
    template_name = 'sales/main.html'
    context_object_name = "sales_list"


class SaleDetailView(DetailView):
    model = Sale
    template_name = "sales/details.html"
    context_object_name = "sale_details"


def sale_details_view(request, pk): # def sale_details_view(request, **kwargs)
    sale_details = Sale.objects.get(pk=pk) # pk = kwargs.get('pk')
    return render(request, 'sales/details.html', {
        'sale_details': sale_details
    })
