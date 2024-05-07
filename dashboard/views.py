from django.shortcuts import render
from django.views.generic import View
from .models import CircleCategory, MainBanner
from .helpers import get_super_categories, get_circle_categories, get_active_banners, get_subbanner, get_mobile_banners, get_left_containers, get_left_sub_images, get_right_containers,get_right_sub_images


class CircleCategoryListCreateView():
    queryset = CircleCategory.objects.all()

class CircleCategoryRetrieveUpdateDestroyView():
    queryset = CircleCategory.objects.all()

class MainBannerListCreateView():
    queryset = MainBanner.objects.all()

class MainBannerRetrieveUpdateDestroyView():
    queryset = MainBanner.objects.all()
    
# Create your views here.
class HomeView(View):
    def get(self, request, **kwargs):
        drop_down_data = get_super_categories()
        #print(drop_down_data)
        circle_data = get_circle_categories()
        banner_data = get_active_banners()
        subbanner = get_subbanner()
        mobilebanner = get_mobile_banners()
        left_container = get_left_containers()
        left_sub_imgs = get_left_sub_images()
        right_container = get_right_containers()
        right_sub_imgs = get_right_sub_images()
        
        context = {
            "drop_down_data": drop_down_data,
            "circle_data": circle_data,
            "banner_data": banner_data,
            "subbanner": subbanner,
            "mobilebanner": mobilebanner,
            "left_container": left_container,
            "left_sub_imgs": left_sub_imgs,
            "right_container": right_container,
            "right_sub_imgs": right_sub_imgs,
        }

        return render(request, 'dashboard/customer_landing.html', context)