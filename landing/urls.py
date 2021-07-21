from django.urls import path
from .views import *

app_name = 'landing'

urlpatterns = [
    path('', index_view, name='index'),
    path('home/', index_view, name='home'),
    path('about/', about_us_view, name='about_us'),
    path('contact/', ContactUsView.as_view(), name='contact_us'),
    path('menu/', MenuItemView.as_view(), name='menu_items'),
    path('orders/', AllOrders.as_view(), name='all_orders'),
    path('orders/<int:pk>', OrderDetails.as_view(), name='order_details'),
    path('orders/add/', AddNewOrder.as_view(), name='add_order'),
    path('messages/', AllMessages.as_view(), name='messages'),
    path('messages/add/', AddMessage.as_view(), name='add_new_message'),

]