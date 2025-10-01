# 📚 Django Model Relationships, Methods, and Properties

## Overview

This Django project demonstrates the use of model relationships, custom methods, and properties. It includes three main
tasks:

1. **ForeignKey Relationship** – Connecting `Author` and `Book` models.
2. **ManyToManyField** – Creating relationships between `Student` and `Course` models.
3. **Model Properties** – Calculating a student's age based on their date of birth.

---

## Task 1: Author and Book (ForeignKey)

- **Models**: `Author`, `Book`
- **Relationship**: Each `Book` is related to one `Author` using a `ForeignKey`.
- **Method**: `Author.get_book_count()` – returns the number of books written by that author.

---

## Task 2: Student and Course (ManyToManyField)

- **Models**: `Student`, `Course`
- **Relationship**: A `Student` can enroll in multiple `Course`s (ManyToMany).
- **Method**: `Student.list_courses()` – returns a list of courses the student is enrolled in.

---

## Task 3: Student Age Property

- **Field**: `date_of_birth` field in the `Student` model.
- **Property**: `Student.age` – calculates the current age based on the date of birth.

---

## How to Run and Test

### 1. Migrate the database

```bash
python manage.py makemigrations
python manage.py migrate
````

### 2. Enter Django shell to test functionality

```bash
python manage.py shell
```

Paste and run the following code:

```python
from app.models import Author, Book, Student, Course
from datetime import date

# Task 1: Create authors and books
author1 = Author.objects.create(name="Author One")
Book.objects.create(title="Book A", author=author1)
Book.objects.create(title="Book B", author=author1)

print("Book count for Author One:", author1.get_book_count())  # Should return 2

# Task 2: Create students and courses
course1 = Course.objects.create(name="Math")
course2 = Course.objects.create(name="History")

student1 = Student.objects.create(name="John Doe", date_of_birth=date(2000, 5, 15))
student1.courses.add(course1, course2)

print("Courses for John Doe:", student1.list_courses())  # Should return list of courses

# Task 3: Check age property
print("John Doe's age:", student1.age)  # Should return the correct age
```

---

## Requirements

* Python 3.13.5
* Django 5.2.5

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Author

This project was created as part of a Django learning assignment focused on model relationships, methods, and
properties.

```


