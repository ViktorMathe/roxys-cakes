from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_cakes, name='cakes'),
    path('add_cake/', views.add_cake, name='add_cake')
]
