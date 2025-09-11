from django.db import models


# Create your models here.
# 1. Author's model
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def book_count(self):
        return self.book_set.count()

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.first_name + " " + self.last_name


# 2. Book's model
class Book(models.Model):
    title = models.CharField(max_length=100)
    # Many - to - One Relationship(ForeignKey), ერთ ავტორს აქვს ბევრი წიგნი
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Author")

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title
