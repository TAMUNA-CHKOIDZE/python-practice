from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='book title')
    author = models.CharField(max_length=100, verbose_name='book author')
    published_date = models.DateField(verbose_name='published date')
    is_deleted = models.BooleanField(default=False, verbose_name='is deleted') # soft delete-ისთვის

    class Meta:
        ordering = ['published_date']  # სორტირება გამოქვეყნების თარიღის მიხედვით
        verbose_name = 'book'
        verbose_name_plural = 'books'
        # ერთი და იგივე ავტორზე არ შეიძლება არსებობდეს ორი წიგნი, რომელსაც ერთი და იგივე სათაური აქვს, მაგრამ სხვადასხვა ავტორებს შეუძლიათ ერთნაირი სახელის წიგნი ჰქონდეთ.
        unique_together = ('title', 'author')

    def __str__(self):
        return self.title
