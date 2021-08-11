from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='items'),
    path('list', views.order_list, name='order_list'),
]