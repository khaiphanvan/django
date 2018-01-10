from django.apps import apps
from django.contrib import admin
from .models import *

class cateAdmin(admin.ModelAdmin):
    fields = ['cate_name','cate_description','cate_status']

admin.site.register(Product)
admin.site.register(Category,cateAdmin)
# Register your models here.
