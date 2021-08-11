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
        "dispatched_orders":dispatched_order,
        "pending_orders":list(pending_order),
    }

    return render(request, "order.html", context)

def sell_item(request, id):
    item = Items.objects.get(id=id)
    quantity = item.quantity
    new_quantity = quantity-1
    if new_quantity == 0:
        new_quantity = 0
        return redirect("items")
    item.quantity = new_quantity
    item.save(update_fields=["quantity"])

    if new_quantity <= 3:
        send_order(id)

        return redirect("items")


    return redirect("items")

def dispatched_order(request, id):
    pending_order = Order.objects.get(id=id)
    item = pending_order.item_id
    item = Items.objects.get(name=item)
    item.quantity = 2
    item.save(update_fields=["quantity"])
    pending_order.dispatch = True
    pending_order.save(update_fields=["dispatch"])

    return redirect("order_list")
    