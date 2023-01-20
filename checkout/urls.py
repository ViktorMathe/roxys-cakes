from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_checkout_session, name='checkout'),
    path('checkout_success/', views.checkout_success, name='checkout_success')

]
