#!/usr/bin/env python
"""Script to create test data for the Django project"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from core.models import Category, Product
from decimal import Decimal

# Create categories
categories_data = [
    'Electronics',
    'Clothing',
    'Home & Garden',
    'Books',
    'Sports & Outdoors'
]

print("Creating categories...")
for cat_name in categories_data:
    category, created = Category.objects.get_or_create(name=cat_name)
    status = "created" if created else "already exists"
    print(f"  - {cat_name}: {status}")

# Create sample products
print("\nCreating sample products...")
products_data = [
    {
        'name': 'Wireless Headphones',
        'category': 'Electronics',
        'price': Decimal('79.99'),
        'description': 'High-quality wireless headphones with noise cancellation and 30-hour battery life.'
    },
    {
        'name': 'Cotton T-Shirt',
        'category': 'Clothing',
        'price': Decimal('29.99'),
        'description': 'Comfortable 100% cotton t-shirt, available in multiple colors and sizes.'
    },
    {
        'name': 'Indoor Plant Pot',
        'category': 'Home & Garden',
        'price': Decimal('24.99'),
        'description': 'Elegant ceramic plant pot with drainage system. Perfect for indoor plants.'
    },
    {
        'name': 'Python Programming Book',
        'category': 'Books',
        'price': Decimal('45.99'),
        'description': 'Comprehensive guide to Python programming for beginners and intermediate developers.'
    },
    {
        'name': 'Yoga Mat',
        'category': 'Sports & Outdoors',
        'price': Decimal('39.99'),
        'description': 'Non-slip yoga mat with carrying strap. Ideal for home or studio practice.'
    }
]

for product_data in products_data:
    category = Category.objects.get(name=product_data['category'])
    product, created = Product.objects.get_or_create(
        name=product_data['name'],
        defaults={
            'category': category,
            'price': product_data['price'],
            'description': product_data['description']
        }
    )
    status = "created" if created else "already exists"
    print(f"  - {product_data['name']}: {status}")

print("\nTest data setup complete!")
print(f"Total Categories: {Category.objects.count()}")
print(f"Total Products: {Product.objects.count()}")
