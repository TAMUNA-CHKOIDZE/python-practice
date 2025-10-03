
# 📚 Book API — Simple Django REST Framework Project

This is a simple API project built using **Django** and **Django REST Framework** as part of a student assignment.

---

## 🎯 Task Requirements

- Install and set up Django REST Framework.
- Add `'rest_framework'` to `INSTALLED_APPS` in `settings.py`.
- Create a simple model: `Book` with the following fields:
  - `title` (CharField)
  - `author` (CharField)
  - `published_date` (DateField)
- Create **two views**:
  1. **Function-based view** to list all books.
  2. **Class-based view** to retrieve a single book by ID.
- Register both views in `urls.py`.

---

## 📦 Project Setup

### 🔧 Requirements

- Python 3.13.5
- Django 5.2.7
- Django REST Framework

### 📁 Installation & Setup

1. Clone the repository  
   To get the project locally, clone the full repository and navigate to the assignment folder:
   ```bash
   git clone https://github.com/TAMUNA-CHKOIDZE/python-practice.git
   cd python-practice/assignment_17
    ```

2. **Create and activate virtual environment**

   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: .\env\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (optional)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

---

## 🧠 API Endpoints

| Method | Endpoint           | Description                 |
| ------ | ------------------ | --------------------------- |
| GET    | `/api/books/`      | List all books (FBV)        |
| GET    | `/api/books/<id>/` | Retrieve a book by ID (CBV) |

---

## 📂 Project Structure

```
book_api/
├── books/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py          # Book model
│   ├── serializers.py     # Book serializer
│   ├── views.py           # Function-based and class-based views
│   ├── urls.py            # App-level routing
├── book_api/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py            # Project-level routing
├── manage.py
```

---

## 🔗 Example Usage

### ✅ List All Books

**GET** `/api/books/`
**Response:**

```json
[
  {
    "id": 1,
    "title": "Django for Beginners",
    "author": "William S. Vincent",
    "published_date": "2021-04-01"
  }
]
```

### ✅ Retrieve Book by ID

**GET** `/api/books/1/`
**Response:**

```json
{
  "id": 1,
  "title": "Django for Beginners",
  "author": "William S. Vincent",
  "published_date": "2021-04-01"
}
```

---

## ✍️ Author

**Tamuna Chkoidze**
Student Project — Django REST Framework Practice

---

## ✅ License

This project is for educational purposes only.

