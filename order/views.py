from django.shortcuts import render, redirect
from .models import Items, Order

# Create your views here.
def item_list(request):
    item_list = Items.objects.all()

    context = {
        "item_list":item_list,
    }
    return render(request, "index.html", context)

def send_order(id):
    item = Items.objects.get(id = id)
    order = Order.objects.create(item_id=item)

    return redirect("items")

def order_list(request):
    dispatched_order = Order.objects.filter(dispatch=True)
    pending_order = Order.objects.filter(dispatch=False)

    context = {
        "dispatched_order":dispatched_order,
        "pending_orders":list(pending_order),
    }

    return render(request, "order.html", context)
