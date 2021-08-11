from django.shortcuts import render, redirect
from .models import Items, Order

# Create your views here.
def item_list(request):
    item_list = Items.objects.all()

    context = {
        "item_list":item_list,
    }
    return render(request, "index.html", context)