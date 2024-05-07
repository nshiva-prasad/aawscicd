from django.db import models
import uuid
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
# Create your models here.


# Common function for upload_to attribute of ImageField
def get_upload_path(instance, filename):
    # Use the model name as the folder name
    return f'{instance.__class__.__name__}/{filename}'


class SuperCategory(models.Model):
    class Meta:
        verbose_name = 'Super Category'
        verbose_name_plural = 'Super Categories'

    name = models.CharField(
        max_length=100, help_text="Please write the name in ALL CAPITALS")
    is_active = models.BooleanField(default=True)
    image = models.ImageField(
        null=True, blank=True, help_text="Please upload an image with dimensions 1080x1080.", upload_to=get_upload_path)

    def __str__(self):
        return self.name


class Category(models.Model):

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=200)
    super_category = models.ManyToManyField(SuperCategory, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Convert the name to uppercase before saving
        self.name = self.name.upper()
        super(Category, self).save(*args, **kwargs)


class SubCategory(models.Model):

    class Meta:
        verbose_name = 'Sub Category'
        verbose_name_plural = 'Sub Categories'

    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category, blank=True)
    super_categories = models.ManyToManyField(SuperCategory)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    product_main_image = models.ImageField(upload_to=get_upload_path)
    description = RichTextUploadingField('Content', null=True, blank=True)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    actual_price = models.DecimalField(max_digits=10, decimal_places=2)
    best_seller = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    number_reviews = models.PositiveIntegerField(null=True, blank=True)
    stock = models.CharField(max_length=20, default='100', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    subcategories = models.ManyToManyField(SubCategory, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    supercategories = models.ManyToManyField(SuperCategory, blank=True)
    
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.name
    
class ProductSubImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sub_images')
    image = models.ImageField(blank=True,upload_to=get_upload_path)

    def get_upload_path(instance, filename):
        return f'{instance.product.__class__.__name__}/{instance.product.product_id}/{filename}'


class ProductTag(models.Model):
    CHOICES = [
        ('text', 'Text'),
        ('date_picker', 'Date Picker'),
        ('image', 'Image'),
        ('multiple_images', 'Multiple Images'),
    ]
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='tagsmain')
    tagname = models.CharField(blank=True,max_length=100)
    tag = models.CharField(blank=True,max_length=100, choices=CHOICES)
    has_color = models.BooleanField(blank=True,default=False)

    def __str__(self):
        return self.tagname

