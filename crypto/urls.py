from django.contrib import admin
from django.urls import path
from .views import index,crypto_table,currency_details,exchange_rates,license

urlpatterns = [
    path('',index,name="index"),
    path('crypto_table',crypto_table,name="cryptotables"),
    path('currency_details',currency_details,name="currency_details"),
    path('exchange_rates',exchange_rates,name="exchange_rates"),
    path('license',license,name="license")
]


