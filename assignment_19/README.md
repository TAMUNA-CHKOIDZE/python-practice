# 🛒 Product API — Filtering, Pagination & Custom Command

This project is a Django REST Framework (DRF) application that demonstrates how to:

- Build a simple API with a `Product` model
- Implement **pagination**
- Add **filtering** by category and price range
- Create a **custom Django management command** to count products in the database

It was developed as part of an assignment to practice DRF fundamentals.

---

## ✅ Features

### 📦 Product Model

The core model includes:

- `name` – product name (`CharField`)
- `category` – predefined choices (e.g. Electronics, Books, Clothing, etc.)
- `price` – decimal value with 2 decimal places

### 📄 Pagination

- Custom pagination class using DRF's `PageNumberPagination`
- Each page displays 4 products by default
- Example:

```

GET /products/products/?page=2

````

### 🔍 Filtering

- Integrated with `django-filter`
- Filter products by:
- `category` (e.g. `/products/products/?category=2`)
- `price` range:
    - `/products/products/?price__gte=50`
    - `/products/products/?price__lte=100`

### 🛠 Custom Management Command

Run the following command to count total products in the database:

```bash
python manage.py count_products
````

Example output:

```
Total Products: 128
```

---

## 🧪 Sample API Request

```
GET /products/products/?category=2&price__lte=100
```

Example response (paginated and filtered):

```json
{
  "count": 7,
  "next": "http://127.0.0.1:8000/products/products/?page=2",
  "previous": null,
  "results": [
    {
      "id": 6,
      "name": "Men's Denim Jacket",
      "category": 3,
      "category_display": "Clothing",
      "price": "55.00",
      "price_with_currency": "55.00 €"
    },
    ...
  ]
}
```

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/TAMUNA-CHKOIDZE/python-practice.git
cd python-practice/assignment_19
```

### 2. Create and activate virtual environment (recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

---

## ✅ Requirements

* Python 3.13.5
* Django 5.2.7
* djangorestframework 3.16.1
* django-filter 25.2

---

## 📁 Project Structure Overview

```
products_project/
├── products/
│   ├── migrations/
│   ├── admin.py
│   ├── choices.py
│   ├── filters.py
│   ├── models.py
│   ├── pagination.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── management/
│       └── commands/
│           └── count_products.py
├── products_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
└── manage.py
```

---

## 📬 Contact

Built with ❤️ by **Tamuna Chkoidze**
This was part of a Django learning assignment.

---

