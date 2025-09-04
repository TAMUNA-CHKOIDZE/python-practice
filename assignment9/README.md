
# 📚 Django Project Initialization Guide

This project is a basic setup for starting a Django web application.


## Requirements

- Python 3.13.5
- Django 5.2.5


## ✅ Steps to Initialize the Project

### 1. Install Django

Make sure you have Python and `pip` installed. Then install Django using pip:

```bash
pip install django
````

### 2. Set up a new Django project

Use the following command to start a new Django project:

```bash
django-admin startproject testproject
cd testproject
```

### 3. Create a Django application

Inside the project folder, run:

```bash
python manage.py startapp testapp
```

### 4. Run initial migrations

Before creating the superuser, apply the migrations:

```bash
python manage.py migrate
```

### 5. Create a Django superuser

To access the Django admin interface, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to set a username, email, and password.

---

## 🚀 Getting Started

To run the development server:

```bash
python manage.py runserver
```

Then open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
The admin interface is available at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📝 Notes

* It's recommended to use a virtual environment for your project.
* Keep `SECRET_KEY` and other sensitive data secure in production.
* Use `.gitignore` to exclude unnecessary files (e.g., `__pycache__`, `.env`, etc.)

---

```
