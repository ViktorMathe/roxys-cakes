from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('subscribe/', views.add_subscriber, name='add_subscriber'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('unsubscribe/', views.remove_from_list, name='unsubscribe')
]
