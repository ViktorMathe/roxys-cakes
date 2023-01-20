from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_cakes, name='cakes'),
    path('add_cake/', views.add_cake, name='add_cake'),
    path('edit_cake/<int:cake_id>', views.edit_cake, name='edit_cake'),
    path('delete_cake/<int:cake_id>', views.delete_cake, name='delete_cake'),
    path('cake_details/<int:cake_id>', views.cake_details, name='cake_details')
]
