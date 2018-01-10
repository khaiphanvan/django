from django import template
from home.models import *

register = template.Library()
@register.filter
def getChilds(parent_id):
    return Category.objects.filter(cate_parent_id=parent_id)

@register.filter
def hasChilds(parent_id):
    childs = Category.objects.filter(cate_parent_id=parent_id)
    if(childs is not None):
        if(len(childs)>0):
            return "True"
    return "False"
