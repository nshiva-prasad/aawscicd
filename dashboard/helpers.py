from .models import *

from inventory.models import Product, ProductSubImage, ProductTag, SuperCategory, Category, SubCategory

def get_super_categories():
    drop_down_data = {}
    drop_down_data = {
        "super_categories": []
    }
    super_categories = SuperCategory.objects.all()

    for super_category in super_categories:
        super_category_data = {
            "name": super_category.name,
            "is_active": super_category.is_active,
            "image_url": str(super_category.image.url) if super_category.image else None,
            "categories": []
        }

        categories = Category.objects.filter(super_category=super_category)

        for category in categories:
            category_data = {
                "name": category.name,
                "sub_categories": []
            }

            sub_categories = SubCategory.objects.filter(category=category, super_categories__in=[super_category])

            for sub_category in sub_categories:
                category_data["sub_categories"].append(
                    {"name": sub_category.name}
                )

            super_category_data["categories"].append(category_data)

        drop_down_data["super_categories"].append(super_category_data)

    return drop_down_data
    

def get_circle_categories():
    circle_categories = CircleCategory.objects.all()
    circle_data = []

    for category in circle_categories:
        circle_item = {
            'id': category.id,
            'circle_image': category.circle_image.url if category.circle_image else None,
            'alt_text': category.alt_text,
            'circle_category_name': category.circle_category_name,
        }
        circle_data.append(circle_item)
    return circle_data


def get_active_banners():
    active_banners = MainBanner.objects.filter(active=True)
    banner_data = [
        {
            'image': banner.image.url,
            'alternate_text': banner.alternate_text,
            'active': banner.active,
        }
        for banner in active_banners
    ]
    return banner_data

def get_subbanner():
    active_sub_banners = SubBanner.objects.filter(active=True)
    sub_banner_urls = {}
    for sub_banner in active_sub_banners:
        sub_banner_urls[sub_banner.id] = {
            'image_url': sub_banner.image.url,
            'alternate_text': sub_banner.alternate_text,
        }
    return sub_banner_urls

def get_mobile_banners():
    active_mobile_banners = MobileBanner.objects.filter(active=True)
    mobile_banners_urls = {}
    for mobile_banner in active_mobile_banners:
        mobile_banners_urls[mobile_banner.id] = {
            'image_url': mobile_banner.image.url,
            'alternate_text': mobile_banner.alternate_text,
        }
    return mobile_banners_urls

def get_left_containers():
    active_left_containers = ImageContainer.objects.filter(is_active=True)
    left_containers_urls = {}
    for left_container in active_left_containers:
        left_containers_urls[left_container.id] = {
            'name' : left_container.name,
            'image_url': left_container.image.url,
            'alternate_text': left_container.alternate_text,
        }

    return left_containers_urls

def get_left_sub_images():
    active_left_sub_images = SubImages.objects.filter(is_active=True)
    left_sub_images_urls = {}
    for left_sub_image in active_left_sub_images:
        left_sub_images_urls[left_sub_image.id] = {
            'title': left_sub_image.title,
            'image_url': left_sub_image.image.url,
            'alternate_text': left_sub_image.alternate_text,
        }

    return left_sub_images_urls

def get_right_containers():
    active_right_containers = ImageContainer.objects.filter(is_active=True)
    right_containers_urls = {}
    for right_container in active_right_containers:
        right_containers_urls[right_container.id] = {
            'name': right_container.name,
            'image_url': right_container.image.url,
            'alternate_text': right_container.alternate_text,
        }

    return right_containers_urls

def get_right_sub_images():
    active_right_sub_images = SubImages.objects.filter(is_active=True)
    right_sub_images_urls = {}
    for right_sub_image in active_right_sub_images:
        right_sub_images_urls[right_sub_image.id] = {
            'title': right_sub_image.title,
            'image_url': right_sub_image.image.url,
            'alternate_text': right_sub_image.alternate_text,
        }

    return right_sub_images_urls


def get_product_detail_data(dispatcher):
    try:
        product = Product.objects.get(product_id=dispatcher)
    except Product.DoesNotExist:
        return None

    sub_images = ProductSubImage.objects.filter(product=product).first()
    
    # Fetch all tags associated with the product using the reverse ManyToMany relationship
    tags = product.tagsmain.all()
    sorted_tags = sorted(tags, key=lambda tag: (
        tag.tag != 'text',
        tag.tag != 'date_picker',
        tag.tag != 'image',
        tag.tag != 'multiple_images',
    ))

    # Prepare the product data
    product_data = {
        'product_id': str(product.product_id),
        'name': product.name,
        'product_main_image': product.product_main_image.url,
        'discounted_price': str(product.discounted_price),
        'actual_price': str(product.actual_price),
        'best_seller': product.best_seller,
        'rating': str(product.rating) if product.rating is not None else None,
        'number_reviews': product.number_reviews,
        'stock': product.stock,
        'created_at': product.created_at,
        'updated_at': product.updated_at,
    }

    # Prepare sub-images data
    sub_images_data = {}
    if sub_images:
        sub_images_data = {
            'sub_image1': sub_images.sub_image1.url if sub_images.sub_image1 else None,
            'sub_image2': sub_images.sub_image2.url if sub_images.sub_image2 else None,
            'sub_image3': sub_images.sub_image3.url if sub_images.sub_image3 else None,
            'sub_image4': sub_images.sub_image4.url if sub_images.sub_image4 else None,
            'sub_image5': sub_images.sub_image5.url if sub_images.sub_image5 else None,
        }
    

    # Prepare product tags data
    tags_data = [{'tagname': tag.tagname, 'tag': tag.tag, 'has_color': tag.has_color} for tag in sorted_tags]

    # Combine all the data
    products_data_list = {
        'product': product_data,
        'sub_images': sub_images_data,
        'tags': tags_data,
    }

    return products_data_list


def get_products_data_by_subcategory(dispatcher):
    products_data = []

    # Get the products that match the subcategory name
    products = Product.objects.filter(SubCategory__name=dispatcher)

    # Loop through the products and create a dictionary for each product
    for product in products:
        product_data = {
            'product_id': str(product.product_id),
            'name': product.name,
            'product_main_image': product.product_main_image.url,
            'discounted_price': float(product.discounted_price),
            'actual_price': float(product.actual_price),
            'best_seller': product.best_seller,
            'rating': float(product.rating) if product.rating is not None else None,
            'number_reviews': product.number_reviews,
            'stock': product.stock,
        }
        products_data.append(product_data)

    return products_data