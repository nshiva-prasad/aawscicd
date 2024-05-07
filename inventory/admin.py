from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


from django.contrib import admin
from .models import Product, ProductSubImage
from .forms import ProductForm

class ProductSubImageInline(admin.StackedInline):
    model = ProductSubImage
    extra = 0
    min_num = 1


from .forms import ProductTagInlineFormSet

class ProductTagInline(admin.TabularInline):
    model = ProductTag
    formset = ProductTagInlineFormSet
    extra = 0
    min_num = 1

class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ('name', 'discounted_price', 'actual_price', 'best_seller', 'rating', 'number_reviews', 'stock')
    list_filter = ('best_seller','name', 'discounted_price', 'actual_price', 'best_seller', 'rating', 'number_reviews', 'stock')
    search_fields = ('name', 'rating')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [ProductSubImageInline,ProductTagInline]

class ProductSubImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'sub_image_preview1', 'sub_image_preview2', 'sub_image_preview3', 'sub_image_preview4', 'sub_image_preview5')

    def sub_image_preview1(self, obj):
        return self._generate_image_preview(obj.sub_image1)

    def sub_image_preview2(self, obj):
        return self._generate_image_preview(obj.sub_image2)

    def sub_image_preview3(self, obj):
        return self._generate_image_preview(obj.sub_image3)

    def sub_image_preview4(self, obj):
        return self._generate_image_preview(obj.sub_image4)

    def sub_image_preview5(self, obj):
        return self._generate_image_preview(obj.sub_image5)

    def _generate_image_preview(self, image_field):
        if image_field:
            return mark_safe(f'<img src="{image_field.url}" alt="{image_field.url}" width="100" height="100"/>')
        else:
            return 'No Image'

    sub_image_preview1.allow_tags = True
    sub_image_preview1.short_description = 'Sub Image 1'

    sub_image_preview2.allow_tags = True
    sub_image_preview2.short_description = 'Sub Image 2'

    sub_image_preview3.allow_tags = True
    sub_image_preview3.short_description = 'Sub Image 3'

    sub_image_preview4.allow_tags = True
    sub_image_preview4.short_description = 'Sub Image 4'

    sub_image_preview5.allow_tags = True
    sub_image_preview5.short_description = 'Sub Image 5'
    
class SuperCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'image_preview')
    readonly_fields = ('image_preview',)
    list_filter = ('is_active',)
    search_fields = ('name',)
    app_label = 'Custom Categories'

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" alt="{obj.name}" width="100" height="100"/>')
        else:
            return '(No image)'
        
    image_preview.short_description = 'Image Preview'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_super_categories')
    list_filter = ('super_category__name',)  # Use the correct field name
    search_fields = ('name',)

    def display_super_categories(self, obj):
        return ', '.join([sc.name for sc in obj.super_category.all()])

    display_super_categories.short_description = 'Super Categories'


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_categories')
    list_filter = ('category__name',)  # Use the correct field name
    search_fields = ('name',)

    def display_categories(self, obj):
        return ', '.join([cat.name for cat in obj.category.all()])

    display_categories.short_description = 'Categories'

admin.site.register(SuperCategory, SuperCategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductSubImage, ProductSubImageAdmin)

