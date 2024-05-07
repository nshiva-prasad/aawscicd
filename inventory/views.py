from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.

from .models import SuperCategory, Category, SubCategory, Product

# Views for SuperCategory model
class SuperCategoryListCreateView():
    queryset = SuperCategory.objects.all()

class SuperCategoryRetrieveUpdateDestroyView():
    queryset = SuperCategory.objects.all()

# Views for Category model
class CategoryListCreateView():
    queryset = Category.objects.all()

class CategoryRetrieveUpdateDestroyView():
    queryset = Category.objects.all()

# Views for Subcategory model
class SubCategoryListCreateView():
    queryset = SubCategory.objects.all()

class SubCategoryRetrieveUpdateDestroyView():
    queryset = SubCategory.objects.all()





# Views for Product model
class ProductListCreateView():
    queryset = Product.objects.all()

class ProductRetrieveUpdateDestroyView():
    queryset = Product.objects.all()
