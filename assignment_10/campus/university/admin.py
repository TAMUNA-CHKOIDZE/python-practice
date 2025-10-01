from django.contrib import admin

from university.models import Author, Book, Student, Course

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Course)