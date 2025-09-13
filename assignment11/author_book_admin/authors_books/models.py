from django.db import models


# Create your models here.
# Author model
class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='First Name')
    last_name = models.CharField(max_length=100, verbose_name='Last Name')
    photo = models.ImageField(upload_to='authors/', verbose_name='Photo')
    nationality = models.CharField(max_length=100, null=True, blank=True, verbose_name='Nationality')
    biography = models.TextField(blank=True, verbose_name='Biography')

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Book and Genre models
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Genre Name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
        ordering = ['name']  # ანბანურად დალაგებს


class Book(models.Model):
    # ForeignKey is Many-to-One: One Author → Many Books and Each Book → One Author
    author = models.ForeignKey(to='Author', on_delete=models.CASCADE, related_name='books', verbose_name='Author')
    # ManyToManyField - ერთი წიგნს შეიძლება ჰქონდეს რამდენიმე ჟანრი. ერთი ჟანრი შეიძლება ეკუთვნოდეს რამდენიმე წიგნს.
    genres = models.ManyToManyField(to='Genre', related_name='books', verbose_name='Genres')
    title = models.CharField(max_length=200, verbose_name='Title')
    published_date = models.DateField(null=True, blank=True, verbose_name='Published Date')
    description = models.TextField(blank=True, verbose_name='Description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
