# API Endpoints & Application Routes

## 🌐 Application Routes

### Main Pages
| Route | URL | View | Purpose |
|-------|-----|------|---------|
| Landing | `/` | `landing()` | Homepage with overview |
| Products | `/products/` | `product_list()` | List all products |
| Product Detail | `/products/<id>/` | `product_detail(id)` | View single product |
| Add Product | `/products/add/` | `add_product()` | Add new product form |
| Admin | `/admin/` | Django Admin | Manage all data |

## 📋 View Functions

### 1. Landing View
```python
URL: /
Method: GET
Returns: landing.html
```

### 2. Product List View
```python
URL: /products/
Method: GET
Returns: product_list.html
Context: {
    'products': All Product objects ordered by -created_at
}
```

### 3. Product Detail View
```python
URL: /products/<int:pk>/
Method: GET
Returns: product_detail.html
Parameters: pk (Product ID)
Context: {
    'product': Single Product object
}
```

### 4. Add Product View
```python
URL: /products/add/
Method: GET/POST
Returns: add_product.html

GET:
- Display form with all categories

POST:
- Accepts: name, category, price, description, image
- Validates fields
- Creates Product record
- Shows success/error message
- Redirects to form
```

## 🏷️ Model Relationships

```
Category (1) -------- (Many) Product
    id                    id
    name                  name
                          category_id (FK)
                          price
                          description
                          image
                          created_at
```

## 📤 Form Fields

### Add Product Form
```
Name: CharField
  - Required: Yes
  - Type: text
  - Placeholder: "Enter product name"

Category: ChoiceField
  - Required: Yes
  - Type: select
  - Source: Category.objects.all()

Price: DecimalField
  - Required: Yes
  - Type: number
  - Step: 0.01
  - Min: 0
  - Prefix: $

Description: CharField
  - Required: No
  - Type: textarea
  - Rows: 4

Image: FileField
  - Required: No
  - Type: file
  - Accept: image/*
  - Max Size: 5MB
```

## 📊 Database Queries

### Get All Products
```python
GET /products/
Query: Product.objects.all().order_by('-created_at')
```

### Get Product by ID
```python
GET /products/<id>/
Query: Product.objects.get(pk=pk)
Raises: Http404 if not found
```

### Add Product
```python
POST /products/add/
Data: name, category_id, price, description, image
Save: Product.objects.create(...)
```

### Filter by Category
```python
Products for Electronics:
Category.objects.get(name='Electronics').products.all()
```

## 🔐 Admin Endpoints

### Category Admin
```
List: /admin/core/category/
Add: /admin/core/category/add/
Edit: /admin/core/category/<id>/change/
Delete: /admin/core/category/<id>/delete/
```

### Product Admin
```
List: /admin/core/product/
Add: /admin/core/product/add/
Edit: /admin/core/product/<id>/change/
Delete: /admin/core/product/<id>/delete/
```

## 💾 Data Models

### Category Model
```python
{
    id: integer (auto-increment),
    name: string (unique, max 100 chars)
}
```

### Product Model
```python
{
    id: integer (auto-increment),
    name: string (max 200 chars),
    category_id: integer (FK to Category),
    price: decimal (10,2),
    description: text (optional),
    image: file path (optional),
    created_at: datetime (auto-set)
}
```

## 📦 Response Examples

### Product List Response
```html
List of products displayed in grid:
- Product cards with images
- Product names
- Categories
- Prices
- View Details buttons
```

### Product Detail Response
```html
Full product page with:
- Large image
- Complete name
- Category badge
- Full price
- Complete description
- Metadata (ID, date)
```

### Add Product Response
```html
Form page with:
- Text input for name
- Category dropdown
- Price input with $ symbol
- Description textarea
- Image file upload
- Submit button
```

## 🎯 URL Patterns

### core/urls.py
```python
urlpatterns = [
    path('', views.landing, name='landing'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/add/', views.add_product, name='add_product'),
]
```

### mysite/urls.py
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

# Media files serving (development only)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## 🔍 Template Context Variables

### product_list.html
```python
{
    'products': QuerySet of Product objects
}
```

### product_detail.html
```python
{
    'product': Single Product object with:
        - id
        - name
        - category (Category object)
        - price
        - description
        - image
        - created_at
}
```

### add_product.html
```python
{
    'categories': QuerySet of Category objects
}
```

## 🛠️ Admin Features

### Product Admin Display
- **List Display:** name, category, price, created_at
- **Filters:** category, created_at
- **Search:** name, description
- **Readonly:** created_at
- **Fieldsets:**
  - Basic Information (name, category, price)
  - Details (description, image)
  - Metadata (created_at)

### Category Admin Display
- **List Display:** name
- **Search:** name

## 📱 Template Features

### Base Template
- Navigation bar with links
- Footer with info
- Bootstrap 5 styling
- Responsive design
- Message display

### Landing Page
- Hero section
- Feature highlights
- Call-to-action buttons

### Product List
- Grid layout
- Product cards
- Image placeholders
- Add product button

### Product Detail
- Full page layout
- Large image
- Complete information
- Navigation buttons

### Add Product
- Form with validation
- File upload
- Category selection
- Message feedback

---

**Note:** All routes are relative to http://127.0.0.1:8000/ in development
