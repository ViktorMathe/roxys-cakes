from django.urls import path
from . import views

urlpatterns = [
    path('', views.bag_view, name='bag_view'),
    path('add/<cake_id>/', views.add_bag_content, name='add_bag_content'),
    path('adjust/<cake_id>', views.change_bag, name='change_bag'),
    path('delete/<cake_id>', views.delete_from_bag, name='delete_from_bag'),

]
