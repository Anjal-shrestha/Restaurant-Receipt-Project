from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import MenuItem,OrderModel
# Create your views here.
def homepage(request):
    items = MenuItem.objects.all()
    return render(request, 'main.html', {'items': items},)

def orderpage(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'order.html', {'menu_items': menu_items})
def menupage(request):
    return render(request,"menu.html")
def aboutpage(request):
    return render(request,"about.html")

def receipt_view(request):
    order_items = {
        'items': []
    }

    items = request.POST.getlist('items[]')
    customer_name = request.POST.get('customer_name')
 
    for item in items:
        menu_item = MenuItem.objects.get(pk=int(item))
        item_data = {
            'id': menu_item.pk,
            'name': menu_item.name,
            'price': menu_item.price,
            'quantity':request.POST.get('quantity-'+str(int(item))),
            'amount': int(menu_item.price) * int(request.POST.get('quantity-'+str(int(item))))
        }
        order_items['items'].append(item_data)

    price = sum(item['amount'] for item in order_items['items'])
    item_ids = [item['id'] for item in order_items['items']]

    order = OrderModel.objects.create(price=price)
    order.items.add(*item_ids)

    context = {
        'items': order_items['items'],
        'price': price,
        'customer_name': customer_name
    }
    print("DEBUG:",context)
    return render(request, 'receipt.html', context)