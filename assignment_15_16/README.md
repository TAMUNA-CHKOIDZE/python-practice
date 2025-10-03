# 🛡️ Custom User and Authentication System in Django

This project demonstrates how to implement a fully customized user model in Django, using email as the unique
identifier  
instead of the default username. It also includes full authentication functionality such as user registration, login,  
logout, session management, and password reset functionality.

---

## ✨ Features

- 🔐 Custom user model using `AbstractBaseUser` and `PermissionsMixin`
- 📧 Email used as the unique login identifier
- 📝 Fields: `email`, `first_name`, `last_name`, `password`
- 🧾 User registration form with validation
- 🔓 Login and logout functionality
- 🔁 Password reset via email with secure token generation
- ✅ Session and permission handling
- 🔁 Redirection logic (e.g., logged-in users can't access register/login pages)
- 📄 Templates for registration, login, password reset, and navigation
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
   cd python-practice/assignment_15_16
    ```

2. Create and Activate Virtual Environment

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Apply Migrations

   ```bash
   python manage.py migrate
   ```

5. Create a Superuser (Optional)

   ```bash
   python manage.py createsuperuser
   ```

6. Run the Development Server

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
* Use the password reset feature from the login page ("Forgot Password?")
* Follow the password reset email link to set a new password

---

## 🧪 Testing

To test the app manually:

* Try registering a new user
* Try logging in with valid and invalid credentials
* Check redirection behavior (e.g., already logged-in user goes to `/register/`)
* Test the password reset flow: request reset, receive email, use link, set new password
* Try logging out and accessing protected pages

---

## 🔧 Custom Password Reset Token Generator

A custom token generator is implemented for secure password reset tokens.
Create a file `utils.py` (or any name you prefer), and add the following:

```python
from django.contrib.auth.tokens import PasswordResetTokenGenerator

class MyPasswordResetTokenGenerator(PasswordResetTokenGenerator):
    pass

# Instantiate the generator to use in views
custom_password_reset_token = MyPasswordResetTokenGenerator()
```

Use `custom_password_reset_token` in your password reset views to generate and check tokens.

---

## 📌 Notes

* The project replaces Django’s default `User` model
* You must reference the custom user model via `AUTH_USER_MODEL` in `settings.py`
* Don't forget to register your user model and forms in the Django admin (if needed)
* Make sure your email backend is configured properly to send password reset emails

---

## 📃 License

This project is for educational purposes and does not currently include a license. Feel free to use and modify for
learning and development.

---

## 👤 Author

Created by **Tamuna Chkoidze**
📧 Email: [chkoidzetamuna1@gmail.com](mailto:chkoidzetamuna1@gmail.com)



