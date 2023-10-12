from rest_framework import serializers
from .models import Book, Genre, Author, Review, FavoritesBook

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BooklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'average_rating']

class BookdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'average_rating', 'description','Reviews__user', 'Reviews__rating', 'Reviews__text']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class FavoritesbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoritesBook
        fields = '__all__'

