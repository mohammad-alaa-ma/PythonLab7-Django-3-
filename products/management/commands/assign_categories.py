from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from products.models import Product
from category.models import Category

class Command(BaseCommand):
    help = 'Assign categories to existing products'

    def handle(self, *args, **options):
        self.stdout.write('Starting category assignment...')
        
        # Check if categories exist
        categories = Category.objects.all()
        if not categories.exists():
            self.stdout.write(
                self.style.ERROR('No categories found! Please create categories first.')
            )
            return
        
        # Check if products exist
        products = Product.objects.all()
        if not products.exists():
            self.stdout.write(
                self.style.WARNING('No products found! Please create products first.')
            )
            return
        
        # Show available categories
        self.stdout.write('\nAvailable categories:')
        for i, category in enumerate(categories, 1):
            self.stdout.write(f'{i}. {category.name} - {category.description}')
        
        # Show products without categories
        products_without_category = products.filter(category__isnull=True)
        if products_without_category.exists():
            self.stdout.write(f'\nProducts without categories: {products_without_category.count()}')
            for product in products_without_category:
                self.stdout.write(f'- {product.name} (Code: {product.code})')
        else:
            self.stdout.write('\nAll products already have categories assigned.')
            return
        
        # Interactive assignment
        self.stdout.write('\nTo assign categories to products:')
        self.stdout.write('1. Go to /admin/ and edit products')
        self.stdout.write('2. Or use the web interface at /products/')
        self.stdout.write('3. Select appropriate categories for each product')
        
        self.stdout.write(
            self.style.SUCCESS('\nCategory assignment guide completed!')
        )
