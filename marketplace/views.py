from django.shortcuts import render,redirect
from marketplace.models import Product,CustomOrder

# Create your views here.


def product_list(request):
    products = Product.objects.all()
    
    category = request.GET.get('category')
    location = request.GET.get('location')
    max_price = request.GET.get('max_price')
    search = request.GET.get('search')

    if category:
        products = products.filter(category__icontains=category)
    if location:
        products = products.filter(location__icontains=location)
    if max_price:
        products = products.filter(price__lte=max_price)
    if search:
        products = products.filter(name__icontains=search)

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        custom_text = request.POST.get('custom_text')
        custom_image = request.FILES.get('custom_image')
        product = Product.objects.get(id=product_id)

        CustomOrder.objects.create(
            product = product,
            custom_text = custom_text,
            custom_image=custom_image
        )

        return redirect('product_list')

    


    return render(request,'list.html',{'products':products})

def mock_payment(request):
    return render(request,'pay.html')

