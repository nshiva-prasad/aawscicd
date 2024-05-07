from .views import *
from django.urls import path
from django.urls import re_path
from inventory import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('create-inventory/', views.create_inventory, name='create_inventory'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)