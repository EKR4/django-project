# Django Product Management System - Class Activity

## Project Overview
This is a complete Django project implementing a product management system with a Category model, Product model, and a user-friendly web interface for managing products.

## ✅ Completed Tasks

### 1. **Models Created**
- **Category Model** (`core/models.py`)
  - `name` - CharField with unique constraint
  - `__str__()` method returns category name
  - Proper Meta class with verbose_name_plural

- **Product Model** (`core/models.py`)
  - `name` - CharField (required)
  - `category` - ForeignKey to Category with CASCADE delete and related_name="products"
  - `price` - DecimalField with 2 decimal places
  - `description` - TextField (optional)
  - `image` - ImageField with upload_to='products/' (optional)
  - `created_at` - DateTimeField with auto_now_add=True
  - `__str__()` method returns product name
  - Proper Meta class with reverse ordering by created_at

### 2. **Database Configuration**
- Configured SQLite database (default)
- Installed Pillow for image field support
- Created and ran migrations:
  - `python manage.py makemigrations` ✓
  - `python manage.py migrate` ✓
- Media files configured in settings.py:
  - `MEDIA_URL = 'media/'`
  - `MEDIA_ROOT = BASE_DIR / 'media'`

### 3. **Admin Interface**
- Registered Category and Product models in `core/admin.py`
- Created CategoryAdmin with:
  - Display list showing name
  - Search functionality by name
- Created ProductAdmin with:
  - Display list showing name, category, price, created_at
  - Filtering by category and created_at
  - Search by name and description
  - Readonly field for created_at
  - Organized fieldsets for better UX

### 4. **Views Created** (`core/views.py`)
- **landing()** - Homepage view
- **product_list()** - Displays all products with pagination-ready template
- **product_detail()** - Shows full details of a single product
- **add_product()** - Form to add new products with image upload support

### 5. **Templates Created**
- **base.html** - Master template with Bootstrap 5 styling
  - Navigation bar with links to all pages
  - Footer with company info and quick links
  - Responsive design for all devices
  - Custom CSS for enhanced styling

- **landing.html** - Homepage
  - Hero section with call-to-action
  - Features section highlighting store benefits
  - Links to products and add product pages

- **product_list.html** - Products listing page
  - Grid layout showing all products
  - Each product card displays:
    - Product image (or placeholder)
    - Product name
    - Category badge
    - Price in green highlight
    - Truncated description
    - Creation date
    - "View Details" button
  - "Add New Product" button in header
  - Empty state message when no products exist

- **product_detail.html** - Product detail page
  - Full product image
  - Complete product information:
    - Name and category
    - Full price and description
    - Full description with line breaks
    - Product ID and creation timestamp
  - Navigation buttons back to product list

- **add_product.html** - Add new product form
  - Form with fields:
    - Product name (required)
    - Category dropdown (required)
    - Price input with $ symbol (required)
    - Description textarea (optional)
    - Image file upload (optional)
  - Success/error messages
  - Form validation
  - Cancel button

### 6. **URL Routing** (`core/urls.py`)
- `/` - Landing page
- `/products/` - Product list view
- `/products/<id>/` - Product detail view
- `/products/add/` - Add new product view

### 7. **Media Configuration**
- Media files served in development mode
- Image uploads go to `media/products/` directory
- Automatic image field support in forms

## 🚀 How to Run

### Prerequisites
- Python 3.8+
- Django 5.2.8
- Pillow (for image support)

### Installation & Setup

1. **Activate Virtual Environment**
   ```bash
   .\.venv\Scripts\Activate.ps1
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   # or manually:
   pip install django pillow djangorestframework
   ```

3. **Create Migrations** (if needed)
   ```bash
   python manage.py makemigrations
   ```

4. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create Superuser** (already done)
   ```bash
   python create_superuser.py
   # Username: admin
   # Password: admin123
   ```

6. **Create Test Data** (already done)
   ```bash
   python create_test_data.py
   ```

7. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**
   - Homepage: http://127.0.0.1:8000/
   - Products: http://127.0.0.1:8000/products/
   - Add Product: http://127.0.0.1:8000/products/add/
   - Admin Panel: http://127.0.0.1:8000/admin/
     - Username: admin
     - Password: admin123

## 📁 Project Structure

```
django-project/
├── core/
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── templates/
│   │   └── core/
│   │       ├── base.html
│   │       ├── landing.html
│   │       ├── product_list.html
│   │       ├── product_detail.html
│   │       └── add_product.html
│   ├── admin.py (✓ Models registered)
│   ├── apps.py
│   ├── models.py (✓ Category & Product models)
│   ├── urls.py (✓ All routes configured)
│   ├── views.py (✓ All views implemented)
│   └── tests.py
├── mysite/
│   ├── settings.py (✓ Media configured)
│   ├── urls.py (✓ Media serving configured)
│   ├── asgi.py
│   └── wsgi.py
├── media/
│   └── products/ (Image upload directory)
├── db.sqlite3 (Database with test data)
├── manage.py
├── create_test_data.py (Helper script)
├── create_superuser.py (Helper script)
└── README.md
```

## ✨ Features Implemented

### Mandatory Requirements
- ✅ Product Model with all required fields
- ✅ Category Model with ForeignKey relationship
- ✅ Image field with Pillow support
- ✅ Created_at timestamp field
- ✅ __str__() methods on both models
- ✅ Migrations created and applied
- ✅ Models registered in admin with proper display
- ✅ Product list view displaying all products
- ✅ Add product functionality
- ✅ Product template showing name, price, image, category

### Optional Features Implemented
- ✅ Product Detail Page with:
  - Full product information
  - Complete description
  - Larger product image display
  - Product metadata (ID, creation date)

### Additional Features
- ✅ Professional Bootstrap 5 UI design
- ✅ Responsive design for mobile and desktop
- ✅ Navigation bar with links to all pages
- ✅ Error handling and success messages
- ✅ Empty state when no products exist
- ✅ Image placeholder when product has no image
- ✅ Admin interface with filtering and search
- ✅ Test data with 5 categories and 5 products
- ✅ Superuser account for admin access

## 🔑 Admin Credentials
- **Username:** admin
- **Password:** admin123

## 📦 Test Data Included
The project comes with pre-populated test data:

**Categories:**
1. Electronics
2. Clothing
3. Home & Garden
4. Books
5. Sports & Outdoors

**Products:**
1. Wireless Headphones - $79.99 (Electronics)
2. Cotton T-Shirt - $29.99 (Clothing)
3. Indoor Plant Pot - $24.99 (Home & Garden)
4. Python Programming Book - $45.99 (Books)
5. Yoga Mat - $39.99 (Sports & Outdoors)

## 🛠️ Technologies Used
- **Django 5.2.8** - Web framework
- **Python 3.13** - Programming language
- **SQLite** - Database
- **Bootstrap 5** - Frontend framework
- **Pillow** - Image processing

## 📝 Notes
- The project uses Django's built-in authentication system
- Media files are served directly from the `media/` directory in development
- All templates use Django template language with Bootstrap 5 styling
- The project follows Django best practices and conventions

## ✅ Class Activity Checklist
- [x] Create Product Model with all required fields
- [x] Create Category Model with ForeignKey
- [x] Install Pillow for image support
- [x] Configure media settings
- [x] Run makemigrations
- [x] Run migrate
- [x] Register models in admin
- [x] Create view for adding products
- [x] Create view for displaying products
- [x] Create product list template
- [x] Create product detail template (optional task)
- [x] Ensure project runs without errors
- [x] Test all functionality

---
**Project Status:** ✅ **COMPLETE** - All requirements met and tested successfully!
