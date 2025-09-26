# 📝 Simple Form with Validation

This project is a simple web page that includes a form to collect a user's **name** and **email address**, with basic
validation to ensure correct input.

## 🔧 Features

* 📄 A form with two fields:

    * **Name** – required field
    * **Email** – must be a valid email address
* ✅ Basic server-side and client-side validation
* 📬 Success and error messages on submission

## 🛠️ Technologies Used

* Python 3.13.5
* Django 5.2.5
* HTML5 / CSS3

## 🚀 How to Run the Project

1. Clone the repository
To get the project locally, clone the full repository and navigate to the assignment folder:
   ```bash
   git clone https://github.com/TAMUNA-CHKOIDZE/python-practice.git
   cd python-practice/assignment13
   ```


2. Install dependencies (for example, with Django):

   ```bash
   pip install -r requirements.txt
   ```

3. Run the development server:

   ```bash
   python manage.py runserver
   ```

4. Open your browser and go to:

   ```
   http://127.0.0.1:8000/
   ```
   

## ✅ Validation Rules

* **Name**: This field is required and cannot be left empty.
* **Email**: Must be a valid email format (e.g., `example@mail.com`).


## 🙋‍♀️ My Contribution

In addition to the basic validation rules, I added custom logic to improve input accuracy:

* The **name** must be **at least 2 characters long**
* It may contain only:
  - **Georgian letters** (`ა-ჰ`)
  - **English letters** (`A–Z`, `a–z`)
  - **Spaces**
  - **Hyphens** (`-`)

✅ Examples of valid names:
- `გიორგი`
- `Nika`
- `გიორგი-ნიკა`

This validation was not part of the original assignment.  
I added it to reflect a real-world data-checking scenario and make the form more robust.

## 💬 Feedback Messages

* A success message is shown when the form is submitted with valid data.
* If there are validation errors, they will be displayed next to the corresponding fields.


