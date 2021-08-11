from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='items'),
    path('<int:id>/selling', views.sell_item, name='selling'),
    path('list', views.order_list, name='order_list'),
    path('<int:id>/dispatch', views.dispatched_order, name='dispatch'),
]