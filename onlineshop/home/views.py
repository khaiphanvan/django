from django.shortcuts import render
from onlineshop.home.models import *
# Create your views here.
def index(request):
    cateParent = Category.objects.filter(cate_parent_id=0)
    featureItems = Product.objects.filter(product_status=1)[:6]
    #categoryItems = Product.
    context = {
        'parents' : cateParent,
        'featureItems': featureItems
    }
    return render(request, "home/index.html",context)