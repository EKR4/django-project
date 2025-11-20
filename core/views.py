# core/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Product, Category


def landing(request):
    return render(request, 'core/landing.html')


def product_list(request):
    """Display all products"""
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'core/product_list.html', context)


def product_detail(request, pk):
    """Display detailed information about a single product"""
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product,
    }
    return render(request, 'core/product_detail.html', context)


def add_product(request):
    """Add a new product (manual form)"""
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            category_id = request.POST.get('category')
            price = request.POST.get('price')
            description = request.POST.get('description', '')
            image = request.FILES.get('image') if 'image' in request.FILES else None
            
            category = get_object_or_404(Category, pk=category_id)
            
            product = Product(
                name=name,
                category=category,
                price=price,
                description=description,
                image=image
            )
            product.save()
            messages.success(request, f'Product "{name}" added successfully!')
            return render(request, 'core/add_product.html', {'categories': Category.objects.all()})
        except Exception as e:
            messages.error(request, f'Error adding product: {str(e)}')
    
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'core/add_product.html', context)
