from django.urls import path
from . import views

urlpatterns = [path('stock-price', views.StockPriceCalculator.as_view(), name='stock')]