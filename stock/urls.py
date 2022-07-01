from django.urls import path
from . import views

urlpatterns = [path('', views.StockPriceCalculator.as_view(), name='stock')]