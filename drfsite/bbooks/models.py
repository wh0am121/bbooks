from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    description = models.TextField()
    average_rating = models.DecimalField(max_digits=3, decimal_places=2)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    text = models.TextField()

class FavoritesBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с пользователем, который добавил книгу
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # Связь с книгой, добавленной в избранное

    def __str__(self):
        return f"{self.user.username}'s Favorite: {self.book.title}"