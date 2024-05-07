from django.core.management.base import BaseCommand
from faker import Faker
from inventory.models import SuperCategory, Category, SubCategory

class Command(BaseCommand):
    help = 'Generate test data for SuperCategory, Category, and SubCategory models'

    def handle(self, *args, **options):
        fake = Faker()

        # Create SuperCategories
        super_categories = []
        for _ in range(8):
            super_category = SuperCategory.objects.create(
                name=fake.name().upper()
            )
            super_categories.append(super_category)

            # Create Categories
            for _ in range(5):
                category = Category.objects.create(
                    name=fake.name().capitalize()
                )
                category.super_category.add(super_category)

                # Create SubCategories
                for _ in range(15):
                    subcategory = SubCategory.objects.create(
                        name=fake.name().capitalize()
                    )
                    subcategory.category.add(category)
                    subcategory.super_categories.add(super_category)

        self.stdout.write(self.style.SUCCESS('Test data generated successfully.'))
