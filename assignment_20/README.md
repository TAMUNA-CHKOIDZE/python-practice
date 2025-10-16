# 📝 Assignment 20 – Django REST Framework: Permissions & Custom Actions

This project demonstrates how to use **custom permissions** and **custom actions** with Django REST Framework using an
`ArticleViewSet`.

## 📌 Task Summary

- Use an existing `ArticleViewSet`.
- Create a custom permission `IsAuthor`, allowing only the article's author to update or delete the article.
- Apply this permission to the ViewSet.
- Add a custom action `publish` that updates the article's `published` field to `True`.

### 🔍 Example Output

- `PUT /articles/3/` → Only works if the logged-in user is the **author** of the article.
- `POST /articles/3/publish/` → Only the author can publish their own article.

---

## ✅ Requirements

* Python 3.13.5
* Django 5.2.7
* djangorestframework 3.16.1

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/TAMUNA-CHKOIDZE/python-practice.git
cd python-practice/assignment_20
````

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> If you don't have `requirements.txt`, install manually:

```bash
pip install django==5.2.7 djangorestframework==3.16.1
```

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create superuser

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

---

## 🔐 Permissions

Custom permission class: `IsAuthor`

```python
class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow only the author to update/delete; others can read
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return obj.author == request.user
        return True
```

Applied to these actions in the ViewSet:

* `update`
* `partial_update`
* `destroy`
* `publish` (custom action)

---

## ⚙️ Custom Action: Publish

Inside `ArticleViewSet`:

```python
@action(detail=True, methods=['post'])
def publish(self, request, pk=None):
    article = self.get_object()
    article.published = True
    article.save(update_fields=['published'])
    return Response({'status': 'published'}, status=status.HTTP_200_OK)
```

---

## 📬 API Endpoints

| Method | Endpoint                | Description                   | Permission    |
|--------|-------------------------|-------------------------------|---------------|
| GET    | /articles/              | List all articles             | Authenticated |
| POST   | /articles/              | Create a new article          | Authenticated |
| GET    | /articles/{id}/         | Retrieve article details      | Authenticated |
| PUT    | /articles/{id}/         | Update article (author only)  | IsAuthor      |
| DELETE | /articles/{id}/         | Delete article (author only)  | IsAuthor      |
| POST   | /articles/{id}/publish/ | Publish article (author only) | IsAuthor      |

---

## ✍️ Author

Tamuna Chkoidze


