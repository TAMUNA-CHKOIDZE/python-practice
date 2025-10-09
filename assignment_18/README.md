
# 🛠️ Flexible Article API with ViewSets and Dynamic Serializers

This Django REST Framework-based project demonstrates how to build a flexible API using `ViewSets`, dynamic `ModelSerializers`, and `DefaultRouter`. The API allows users to request only specific fields in list/detail views, handle all CRUD operations, and supports soft-deletion of articles.

---

## ✅ Requirements

* Python 3.13.5  
* Django 5.2.7  
* djangorestframework 3.16.1  

---

## 🚀 Getting Started

### 1. Clone the repository

To get the project locally, clone the full repository and navigate to the assignment folder:

```bash
git clone https://github.com/TAMUNA-CHKOIDZE/python-practice.git
cd python-practice/assignment_18
````

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, manually install:

```bash
pip install Django==5.2.7 djangorestframework==3.16.1
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create superuser (optional)

```bash
python manage.py createsuperuser
```

### 6. Run the server

```bash
python manage.py runserver
```

---

## 📦 Project Structure

```bash
assignment_18/
├── project/
│   ├── articles/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── project/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── manage.py
├── requirements.txt
└── README.md
```

---

## 📚 Functionality Overview

### 🔧 Model

The `Article` model contains:

* `title` – CharField
* `content` – TextField
* `author` – CharField
* `published_date` – DateTimeField (auto_now_add)
* `article_deleted` – BooleanField (for soft delete)

### 📤 Serializer

The `ArticleSerializer` inherits from a `DynamicFieldsModelSerializer`, which allows dynamic field filtering using query parameters like:

```
?fields=title,author
```

This enables you to return only the requested fields in both list and detail views.

### 🔄 ViewSet

`ArticlesViewSet` supports:

* Dynamic field selection based on request context.
* Soft-deletion via the `destroy` method (marks `article_deleted=True` instead of deleting).
* Default queryset excludes deleted articles.

---

## 🔍 Example API Requests

### List Articles (Excludes `content` field by default):

```
GET /articles/
```

### List Articles with Specific Fields:

```
GET /articles/?fields=title,author
```

### Retrieve Full Article by ID:

```
GET /articles/1/
```

### Retrieve Specific Fields in Detail View:

```
GET /articles/1/?fields=title,published_date
```

### Create an Article:

```
POST /articles/
Content-Type: application/json

{
  "title": "New Article",
  "content": "This is the content.",
  "author": "John Doe"
}
```

### Soft Delete Article:

```
DELETE /articles/1/
```

---

## 🛠 Admin Panel

To manage articles via the Django admin interface:

1. Run the server: `python manage.py runserver`
2. Open: `http://127.0.0.1:8000/admin/`
3. Login with your superuser credentials

---

## 🧪 Testing Tips

* Use **Postman** or **cURL** to test dynamic field querying.
* Articles marked as `article_deleted=True` will not be listed or retrieved.

---

## 📝 Notes

* No pagination or permissions are added, but this project can be extended with those features.
* Using `exclude = ['article_deleted']` in the serializer ensures it's not exposed via the API.

---

## 📫 Author

**Tamuna Chkoidze**
[GitHub Repository](https://github.com/TAMUNA-CHKOIDZE/python-practice)

