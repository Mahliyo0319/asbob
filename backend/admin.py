from django.contrib import admin
from backend.models import *

# Register your models here.
class Header_slider_Admin(admin.ModelAdmin):
    list_display=['title', 'created_by']

class Product_admin(admin.ModelAdmin):
    list_display=['Rate','name','price','discount','availability',]
    list_editable=['availability','discount']

admin.site.register(Header_slider,Header_slider_Admin)
admin.site.register(Models)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product,Product_admin)

