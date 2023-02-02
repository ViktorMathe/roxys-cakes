from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout_session, name='checkout'),
    path('cache_checkout_session/',
         views.cache_checkout_session, name='cache_checkout_session'),
    path('checkout_success/<order_number>',
         views.checkout_success, name='checkout_success'),
    path('webhook/', webhook, name='webhook'),
]
