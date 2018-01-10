from django.shortcuts import render
from home.models import *
# Create your views here.
def index(request):
    cateParent = Category.objects.filter(cate_parent_id=0)
    context = {
        'parents' : cateParent
    }
    return render(request, "home/index.html",context)