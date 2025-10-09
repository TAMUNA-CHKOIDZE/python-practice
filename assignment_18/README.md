
# 🛠️ Flexible Article API with ViewSets and Dynamic Serializers

This project demonstrates how to build a flexible and powerful RESTful API in Django using **ViewSets**, **ModelSerializers with dynamic fields**, and **DRF routers**.

The main feature is the ability to dynamically include specific fields in the API response via query parameters like `?fields=title,author`.

---

## 📦 Features

- Full CRUD operations for an `Article` model
- Dynamic fields in serializers using `?fields=` query parameter
- Clean URL routing using `DefaultRouter` from Django REST Framework

---

## 🧩 Model Structure

The API is built around a simple `Article` model with the following fields:

```python
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100)
    published = models.DateTimeField(auto_now_add=True)
```

---

## 🔄 API Behavior

### 🔍 Dynamic Field Filtering

You can filter the fields returned by the API using the `?fields=` query parameter:

* `GET /articles/?fields=title,author`
  → returns only the `title` and `author` of each article.

* `GET /articles/1/`
  → returns **all fields** of the article with ID 1.

* `POST /articles/`
  → creates a new article (send full data in request body).

---

## 🛠️ Installation & Setup

1. Clone the repository  
   To get the project locally, clone the full repository and navigate to the assignment folder:
   ```bash
   git clone https://github.com/TAMUNA-CHKOIDZE/python-practice.git
   cd python-practice/assignment_18
    ```

2. **Set up a virtual environment and install dependencies**

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

3. **Apply migrations**

```bash
python manage.py migrate
```

4. **Run the development server**

```bash
python manage.py runserver
```

---

## 🧪 Example Requests

### ✅ Get all articles (default/full response)

```http
GET /articles/
```

### ✅ Get only selected fields

```http
GET /articles/?fields=title,author
```

### ✅ Get single article by ID

```http
GET /articles/1/
```

### ✅ Create a new article

```http
POST /articles/
Content-Type: application/json

{
  "title": "Hello World",
  "content": "This is a new article.",
  "author": "John Doe"
}
```

---

## 📁 File Structure Overview

```
project/
├── articles/
│   ├── models.py         # Article model
│   ├── serializers.py    # Dynamic serializer logic
│   ├── views.py          # ViewSet with dynamic serializer
│   └── urls.py           # Router-based URL config
├── project/
│   └── settings.py       # Standard Django settings
├── manage.py
└── README.md             # This file
```

---

## 🧠 How It Works

### Dynamic Serializer Logic

In `serializers.py`, we override the `__init__` method to accept a `fields` parameter:

```python
class DynamicArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
```

In `views.py`, we extract the `fields` from the request:

```python
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = DynamicArticleSerializer

    def get_serializer(self, *args, **kwargs):
        fields = self.request.query_params.get('fields')
        if fields:
            fields = [f.strip() for f in fields.split(',')]
            kwargs['fields'] = fields
        return super().get_serializer(*args, **kwargs)
```

---

## 🔗 Routes

Using `DefaultRouter` or `SimpleRouter`, routes are auto-generated like:

```
/articles/       -> List & Create
/articles/{id}/  -> Retrieve, Update, Delete
```

---

## ✅ Requirements

* Python 3.13.5
* Django 5.2.7
* Django REST Framework

Install dependencies using:

```bash
pip install django djangorestframework
```

---

## 📚 License

This project is for educational purposes. Free to use and modify.

---

## 🙋‍♂️ Need Help?

Feel free to open an issue or reach out with questions!

```
