from django.shortcuts import render
from marketplace.models import CustomOrder


# Create your views here.


def buyer_dashboard(request):
    orders = CustomOrder.objects.filter(user=request.user).order_by('-created_at')
    return render(request,'buy.html',{'orders':orders})