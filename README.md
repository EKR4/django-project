# Django Product Management System 🛍️

A complete Django project implementing a product management system with categories, product listing, and admin interface.

## 🎯 Project Status: ✅ **COMPLETE**

This project was built as a **Django Class Activity** with all requirements met and tested.

## 🌟 Key Features

- ✅ **Product Model** with image support
- ✅ **Category Model** with ForeignKey relationship
- ✅ **Admin Interface** for managing products and categories
- ✅ **Product Listing** page with grid layout
- ✅ **Product Detail** page with full information
- ✅ **Add Product** form with image upload
- ✅ **Bootstrap 5** responsive design
- ✅ **Test Data** included with 5 categories and 5 products

## 🚀 Quick Start

### Installation
```bash
# Clone the repository
git clone https://github.com/EKR4/django-project.git
cd django-project

# Create virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python create_superuser.py

# Create test data
python create_test_data.py

# Start server
python manage.py runserver
```

### Access Application
- **Homepage:** http://127.0.0.1:8000/
- **Products:** http://127.0.0.1:8000/products/
- **Add Product:** http://127.0.0.1:8000/products/add/
- **Admin Panel:** http://127.0.0.1:8000/admin/
  - Username: `admin`
  - Password: `admin123`

## 📁 Project Structure

```
django-project/
├── core/
│   ├── models.py         # Product & Category models
│   ├── views.py          # All views
│   ├── admin.py          # Admin configuration
│   ├── urls.py           # URL routing
│   ├── templates/core/   # HTML templates
│   └── migrations/       # Database migrations
├── mysite/
│   ├── settings.py       # Project settings
│   ├── urls.py           # Main URL config
│   └── ...
├── db.sqlite3            # Database with test data
└── manage.py
```

## 📚 Documentation Files

- **[CLASS_ACTIVITY_COMPLETE.md](CLASS_ACTIVITY_COMPLETE.md)** - Complete project overview
- **[QUICK_START.md](QUICK_START.md)** - Quick reference guide
- **[API_ENDPOINTS.md](API_ENDPOINTS.md)** - Routes and endpoints documentation
- **[SUBMISSION.md](SUBMISSION.md)** - Final submission details

## 🛠️ Technologies

- Django 5.2.8
- Python 3.13
- SQLite3
- Bootstrap 5
- Pillow (Image processing)

## 📊 Included Test Data

### Categories
1. Electronics
2. Clothing
3. Home & Garden
4. Books
5. Sports & Outdoors

### Sample Products
1. Wireless Headphones ($79.99)
2. Cotton T-Shirt ($29.99)
3. Indoor Plant Pot ($24.99)
4. Python Programming Book ($45.99)
5. Yoga Mat ($39.99)

## ✅ Requirements Checklist

- [x] Create Product Model with all required fields
- [x] Create Category Model with ForeignKey
- [x] Install Pillow for image support
- [x] Configure database
- [x] Run makemigrations and migrate
- [x] Register models in admin
- [x] Create product listing view
- [x] Create product detail view
- [x] Create add product functionality
- [x] Create templates
- [x] Configure URL routing
- [x] Test all functionality
- [x] Push to GitHub

## 🔗 GitHub Repository

**Repository:** https://github.com/EKR4/django-project

**Branch:** `product-model-feature`

**Current Status:** Ready for deployment

## 💬 Usage Examples

### View All Products
```
GET /products/
```

### View Single Product
```
GET /products/1/
```

### Add New Product
```
POST /products/add/
Form Fields: name, category, price, description, image
```

### Admin Access
```
GET /admin/
Login with: admin / admin123
```

## 🎓 Class Activity Completion

This project was built following Django best practices and CLI commands:

1. Created models using Django ORM
2. Generated migrations with `makemigrations`
3. Applied migrations with `migrate`
4. Created views for CRUD operations
5. Designed templates with Bootstrap 5
6. Registered models in admin interface
7. Configured URL routing
8. Tested all functionality
9. Pushed code to GitHub

## ⚡ Running the Project

```bash
# Activate environment
.\.venv\Scripts\Activate.ps1

# Start server
python manage.py runserver

# Server runs at http://127.0.0.1:8000/
```

## 📝 Notes

- All required fields are properly validated
- Image uploads are handled securely
- Admin interface is fully functional
- Test data is pre-populated
- Responsive design works on all devices

---

**Status:** ✅ Complete and running | **Last Updated:** November 20, 2025
