from django.urls import path
from .views import (
    home_view, SaleListView, SaleDetailView, sale_details_view
)

app_name = 'sales'

urlpatterns = [
    path('', home_view, name='home'),
    path('sales/', SaleListView.as_view(), name='main'),
    path('sales/<pk>/', sale_details_view, name='detail')
]
