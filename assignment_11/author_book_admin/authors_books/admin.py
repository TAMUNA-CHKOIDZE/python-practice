from django.contrib import admin

from authors_books.models import Author, Book, Genre


# Register your models here.
# Author, Book და Genre ყველა რეგისტრირებულია @admin.register დეკორატორით.

class BookInline(admin.TabularInline):
    model = Book
    extra = 1  # რამდენი ახალი ჩანაწერის ველა გამოჩნდეს დამატებისთვის


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
     # ავტორებში იქნება Books განყოფილება და Add another Book-ს
    inlines = [BookInline]
    list_display = ('full_name', 'nationality')
    search_fields = ('first_name', 'last_name',)
    list_filter = ('first_name', 'last_name', 'nationality')


# ასარჩევი სიის სახით რომ მქონდეს ჟანრი
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'get_genres')
    search_fields = ('title',)
    list_filter = ('published_date', 'genres')
    filter_horizontal = ('genres',)  # უკეთესი UI ManyToMany ველისთვის

    @admin.display(description='Genres')
    def get_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)