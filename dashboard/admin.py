from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
# Register your models here.

class CircleCategoryAdmin(admin.ModelAdmin):
    list_display = ('circle_image_preview', 'alt_text', 'circle_category_name')
    readonly_fields = ('circle_image_preview',)

    def circle_image_preview(self, obj):
        if obj.circle_image:
            return mark_safe(f'<img src="{obj.circle_image.url}" alt="{obj.alt_text}" width="100" height="100"/>')
        else:
            return 'No Image'
    circle_image_preview.allow_tags = True
    circle_image_preview.short_description = 'Circle Image Preview'
    
class BannerAdmin(admin.ModelAdmin):
    list_display = ('banner_image_preview', 'alternate_text', 'active')
    readonly_fields = ('banner_image_preview',)

    def banner_image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" alt="{obj.alternate_text}" width="200" height="100"/>')
        else:
            return 'No Image'

    banner_image_preview.allow_tags = True
    banner_image_preview.short_description = 'Banner Image Preview'


class SubBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview', 'active')
    list_filter = ('active',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" alt="SubBanner {obj.id}" width="500" height="100"/>')
        else:
            return 'No Image'

    image_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'

class MobileBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview', 'active')
    list_filter = ('active',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" alt="SubBanner {obj.id}" width="550" height="100"/>')
        else:
            return 'No Image'

    image_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'


    
class ImageContainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_preview', 'is_active')
    list_filter = ('name','is_active',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" alt="{obj.name}" width="100" height="150"/>')
        else:
            return 'No Image'

    image_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'
    

class SubImagesAdmin(admin.ModelAdmin):
    list_display = ('container', 'title', 'image_preview', 'is_active')
    list_filter = ('container', 'title', 'is_active')

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" alt="{obj.title}" width="100" height="100"/>')
        else:
            return 'No Image'

    image_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'
    
    
admin.site.register(CircleCategory, CircleCategoryAdmin)
admin.site.register(MainBanner,BannerAdmin)
admin.site.register(SubBanner,SubBannerAdmin)
admin.site.register(MobileBanner,MobileBannerAdmin)
admin.site.register(ImageContainer, ImageContainerAdmin)
admin.site.register(SubImages, SubImagesAdmin)