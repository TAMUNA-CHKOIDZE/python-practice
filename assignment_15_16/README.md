# 🛡️ Custom User and Authentication System in Django

This project demonstrates how to implement a fully customized user model in Django, using email as the unique identifier
instead of the default username. It also includes full authentication functionality such as user registration, login,
logout, and session management.

---

## ✨ Features

- 🔐 Custom user model using `AbstractBaseUser` and `PermissionsMixin`
- 📧 Email used as the unique login identifier
- 📝 Fields: `email`, `first_name`, `last_name`, `password`
- 🧾 User registration form with validation
- 🔓 Login and logout functionality
- ✅ Session and permission handling
- 🔁 Redirection logic (e.g., logged-in users can't access register/login pages)
- 📄 Templates for registration, login, and navigation
- ⚠️ CSRF protection and error messages

---

## 🛠️ Technologies Used

- Python 3.13.5
- Django 5.2.5
- HTML5 / CSS3
- SQLite (default Django database)

---

## 🚀 How to Run the Project

1. Clone the repository
   To get the project locally, clone the full repository and navigate to the assignment folder:
   ```bash
   git clone https://github.com/TAMUNA-CHKOIDZE/python-practice.git
   cd python-practice/assignment15
   ```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

---

## ✅ How to Use

* Visit `/register/` to create a new account
* Login at `/login/` using your email and password
* Logout at `/logout/`
* Access protected views only when logged in
* Registered/logged-in users are redirected away from login/register pages

---

## 🧪 Testing

To test the app manually:

* Try registering a new user
* Try logging in with valid and invalid credentials
* Check redirection behavior (e.g., already logged-in user goes to `/register/`)
* Try logging out and accessing protected pages

---

## 📌 Notes

* The project replaces Django’s default `User` model
* You must reference the custom user model via `AUTH_USER_MODEL` in `settings.py`
* Don't forget to register your user model and forms in the Django admin (if needed)

---

## 📃 License

This project is for educational purposes and does not currently include a license. Feel free to use and modify for
learning and development.

---

## 👤 Author

Created by **Tamuna Chkoidze**
📧 Email: [chkoidzetamuna1@gmail.com](mailto:chkoidzetamuna1@gmail.com)

