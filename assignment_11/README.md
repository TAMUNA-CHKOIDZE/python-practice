
# Django Admin Customization

## 📚 Project Description

This project demonstrates how to register and customize Django models in the admin interface. Two models, **Author** and **Book**, are defined, registered in the Django admin site, and customized to enhance data management. Admin interface is enhanced using features like list display, search fields, and filtering options.

## ✅ Requirements

* Python 3.13.5
* Django 5.2.5

> Ensure you have a virtual environment activated before installing dependencies.


## ⚙️ Setup Instructions

1. Clone the repository
To get the project locally, clone the full repository and navigate to the assignment folder:
   ```bash
   git clone https://github.com/TAMUNA-CHKOIDZE/python-practice.git
   cd python-practice/assignment_11
   ```

2. **Go to the assignment folder** (for this task: `assignment11`):

   ```bash
   cd assignment11
   ```

3. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # on Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install django==5.2.5
   ```

4. **Run migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the admin panel:**

   Visit `http://127.0.0.1:8000/admin` and log in with your superuser credentials.

## 🧩 Models

### Author

Fields:

* `name` (CharField)
* `birth_date` (DateField)

### Book

Fields:

* `title` (CharField)
* `author` (ForeignKey to Author)
* `published_date` (DateField)
* `genre` (CharField)

## 🛠️ Admin Customization

In `admin.py`, the following customizations are implemented:

### For `AuthorAdmin`:

* `list_display = ['name', 'birth_date']`
* `search_fields = ['name']`

### For `BookAdmin`:

* `list_display = ['title', 'author', 'published_date', 'genre']`
* `search_fields = ['title', 'author__name']`
* `list_filter = ['published_date', 'genre']`

These enhancements allow for easier management of data in the Django admin interface.

