# from csv import list_dialects
from django.contrib import admin

# Register your models here.

from .models import Category,ProductImage,SizeVariant,Product,ColorVariant




admin.site.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}

class ProductImageAdmin(admin.StackedInline):
    model =ProductImage
admin.site.register(Product )
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name' , 'price','category' ]
    prepopulated_fields={'slug':('name',)}
    
    # inlines = [ProductImageAdmin]


@admin.register(ColorVariant)
class ColorVariantAdmin(admin.ModelAdmin):
    list_display = ['color_name' , 'price']
    model = ColorVariant

@admin.register(SizeVariant)
class SizeVariantAdmin(admin.ModelAdmin):
    list_display = ['size_name' , 'price']

    model = SizeVariant


# admin.site.register(Product ,ProductAdmin)


admin.site.register(ProductImage)