from django.shortcuts import render, get_list_or_404, reverse
from django.views import View, generic
from .models import *
from django.http import Http404, HttpResponse


# Create your views here.


def index_view(request):

    return render(request, 'landing/home.html')

def about_us_view(request):

    return render(request, 'landing/about_us.html')

class ContactUsView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'landing/contact.html')

    def post(self):
        ...


class MenuItemView(generic.ListView):

    template_name = 'landing/menu_list.html'
    model = MenuItem
    context_object_name = 'all_menu_items'


class AddNewOrder(generic.CreateView):

    template_name = 'landing/add_order.html'
    model = Order
    fields = ['table_id', 'menu_item_id', 'menu_item_number']

    def get_success_url(self):
        return reverse('landing:all_orders')


class AllOrders(generic.ListView):

    template_name = 'landing/all_orders.html'
    model = Order
    context_object_name = 'orders_list'


class OrderDetails(generic.DetailView):

    template_name = 'landing/order_detail.html'
    model = Order
    context_object_name = 'o_detail'


class AddMessage(generic.CreateView):

    template_name = 'landing/add_message.html'
    model = Message
    fields = ['customer_name', 'email', 'message_text']

    def get_success_url(self):
        return reverse('landing:messages')


class AllMessages(generic.ListView):

    template_name = 'landing/all_messages.html'
    model = Message
    context_object_name = 'message_list'


