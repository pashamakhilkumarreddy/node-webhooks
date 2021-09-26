from django import forms
from django.forms import widgets
from collections import namedtuple

CHOICE = namedtuple('CHOICE', 'Serial_Number Type')

CHART_CHOICES = (
    CHOICE('#1', 'Bar Chart'),
    CHOICE('#2', 'Pie Chart'),
    CHOICE('#3', 'Line Chart')
)

class SalesSearchForm(forms.Form):
    date_form = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    chart_type = forms.ChoiceField(choices=CHART_CHOICES)