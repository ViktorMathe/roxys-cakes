from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_us, name='contact_us'),
    path('messages/', views.contact_messages, name='messages')
]
