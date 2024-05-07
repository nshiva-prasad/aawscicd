from django.db import models


# Common function for upload_to attribute of ImageField
def get_upload_path(instance, filename):
    # Use the model name as the folder name
    return f'{instance.__class__.__name__}/{filename}'


# Model for the dropdown menu and stuff


# Create your models here.
class CircleCategory(models.Model):
    class Meta:
        verbose_name = 'Circle Category'
        verbose_name_plural = 'Circle Categories'

    circle_image = models.ImageField(
        null=True, blank=True, help_text="Please upload an image with dimensions 1080x1080.", upload_to=get_upload_path)
    alt_text = models.CharField(
        max_length=100, help_text="Please provide the alternate text to display")
    circle_category_name = models.CharField(
        max_length=50, help_text="This is the text that appears below the Circle")

    def __str__(self):
        return self.circle_category_name


class MainBanner(models.Model):
    class Meta:
        verbose_name = 'Main Banner'
        verbose_name_plural = 'Main Banners'

    image = models.ImageField(upload_to=get_upload_path)
    alternate_text = models.CharField(max_length=255)
    active = models.BooleanField(default=False)


class SubBanner(models.Model):
    class Meta:
        verbose_name = 'SubBanner'
        verbose_name_plural = 'SubBanner'
    image = models.ImageField(upload_to=get_upload_path)
    alternate_text = models.CharField(max_length=255, null=True)
    active = models.BooleanField(default=False)


class MobileBanner(models.Model):
    class Meta:
        verbose_name = 'MobileBanner'
        verbose_name_plural = 'MobileBanner'
    image = models.ImageField(upload_to=get_upload_path)
    alternate_text = models.CharField(max_length=255, null=True)
    active = models.BooleanField(default=False)


class ImageContainer(models.Model):
    class Meta:
        verbose_name = 'Image Container'
        verbose_name_plural = 'Image Containers'

    SIDE_CHOICES = [
        ('left', 'Left'),
        ('right', 'Right'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=get_upload_path)
    alternate_text = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    side = models.CharField(max_length=5, choices=SIDE_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.get_side_display()})"

class SubImages(models.Model):
    class Meta:
        verbose_name = 'Sub Image'
        verbose_name_plural = 'Sub Images'

    container = models.ForeignKey(ImageContainer, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_upload_path)
    alternate_text = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)