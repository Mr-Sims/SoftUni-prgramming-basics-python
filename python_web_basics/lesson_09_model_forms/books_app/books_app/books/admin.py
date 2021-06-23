from django.contrib import admin

from books_app.books.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']


admin.site.register(Book, BookAdmin)
