# Quick Start Guide - Adding Products

## Access the Application

1. **Start the server** (if not already running):
   ```bash
   python manage.py runserver
   ```

2. **Open your browser** and navigate to:
   - **Homepage:** http://127.0.0.1:8000/
   - **Products Page:** http://127.0.0.1:8000/products/
   - **Admin Panel:** http://127.0.0.1:8000/admin/

## Adding Products via Web Form

### Method 1: Using the "Add New Product" Button
1. Go to http://127.0.0.1:8000/products/
2. Click the **"Add New Product"** button (green button in top right)
3. Fill in the form:
   - **Product Name** (required) - e.g., "Laptop"
   - **Category** (required) - Select from dropdown (e.g., "Electronics")
   - **Price** (required) - e.g., "999.99"
   - **Description** (optional) - Add detailed info about the product
   - **Image** (optional) - Upload a product image (JPG, PNG, GIF)
4. Click **"Add Product"** button
5. You'll see a success message and the form will clear

### Method 2: Using Direct Link
- Navigate directly to: http://127.0.0.1:8000/products/add/

## Adding Products via Admin Panel

### Step 1: Login to Admin
1. Go to http://127.0.0.1:8000/admin/
2. Login with:
   - Username: **admin**
   - Password: **admin123**

### Step 2: Add Product
1. Click on **"Products"** in the left sidebar
2. Click **"Add product"** button (top right)
3. Fill in all the fields:
   - Name
   - Category (select from dropdown)
   - Price
   - Description
   - Image (upload from computer)
4. Click **"Save"** button

### Step 3: View the Product
After adding:
- Go to http://127.0.0.1:8000/products/ to see it in the product list
- Click "View Details" to see the full product page

## Adding Categories via Admin

If you need to add more categories:

1. Login to admin panel (http://127.0.0.1:8000/admin/)
2. Click on **"Categories"** in the left sidebar
3. Click **"Add category"** button
4. Enter the category name
5. Click **"Save"**

## View Your Products

### Product List Page
- **URL:** http://127.0.0.1:8000/products/
- Shows all products in a grid layout
- Click "View Details" on any product card to see full information

### Product Detail Page
- **URL:** http://127.0.0.1:8000/products/<product_id>/
- Example: http://127.0.0.1:8000/products/1/
- Shows:
  - Large product image
  - Full product name
  - Category badge
  - Complete price
  - Full description
  - Product metadata (ID, creation date)

## Features

### Product List
- Grid layout with product cards
- Each card shows:
  - Product image (or placeholder)
  - Product name
  - Category
  - Price
  - Truncated description
  - Creation date
  - "View Details" link

### Product Detail
- Large image view
- Full product information
- Complete description
- All metadata
- Navigation back to product list

### Form Validation
- Required fields are marked with red asterisk (*)
- Price must be a valid number with 2 decimal places
- Category selection is mandatory
- Image upload is optional (supports JPG, PNG, GIF)

## Troubleshooting

### Image Not Uploading?
1. Make sure the file is in JPG, PNG, or GIF format
2. File size should be reasonable (typically < 5MB)
3. Check browser console for any error messages

### Product Not Appearing?
1. Refresh the products page (F5 or Ctrl+R)
2. Check that all required fields were filled
3. Verify the product was saved successfully (you should see a success message)

### Can't Login to Admin?
- Username: **admin**
- Password: **admin123**
- Make sure you're going to http://127.0.0.1:8000/admin/

## Database Reset (if needed)

To reset the database and start fresh:
```bash
# Delete the old database
del db.sqlite3

# Recreate migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python create_superuser.py

# Add test data
python create_test_data.py
```

---

**Happy Adding!** 🎉 Your product management system is ready to use!
