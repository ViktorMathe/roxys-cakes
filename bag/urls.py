from django.urls import path
from . import views

urlpatterns = [
    path('', views.bag, name='bag'),
    path('add/<cake_id>/', views.bag_content, name='bag_content')

]
