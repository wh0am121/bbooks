from django.contrib import admin
from .models import Genre, Author, Book, Review, FavoritesBook

admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(FavoritesBook)
# Register your models here.
