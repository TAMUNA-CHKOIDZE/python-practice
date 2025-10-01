from datetime import date

from django.db import models


# Create your models here.
# 1. Author's model
class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")

    def book_count(self):
        # აბრუნებს კონკრეტული ავტორის წიგნების რაოდენობას
        return self.books.count()  # related_name='books'

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.first_name + " " + self.last_name


# 2. Book's model
class Book(models.Model):
    title = models.CharField(max_length=100)
    # Many - to - One Relationship(ForeignKey), ერთ ავტორს აქვს ბევრი წიგნი
    author = models.ForeignKey(to='Author', on_delete=models.CASCADE, verbose_name="Author", related_name='books')

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.title


class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    birth_date = models.DateField(verbose_name="Birth Date", null=True)
    # Student-ს აქვს ManyToManyField კავშირი კურსებთან
    courses = models.ManyToManyField(Course, related_name='students', verbose_name="Courses")

    @property
    def age(self):
        today = date.today()
        return today.year - self.birth_date.year - (
                (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # list_courses method return lists all the courses a student is enrolled in.
    def list_courses(self):
        return [course.title for course in self.courses.all()]
