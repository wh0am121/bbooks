from django.forms import model_to_dict
from rest_framework import generics
from .models import Book, Genre, Author, Review, FavoritesBook
from .serializers import BooklistSerializer
from .serializers import BookdetailSerializer
#GenreSerializer, AuthorSerializer, ReviewSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class BookList(APIView):
    def get(self, request):
        lst = Book.objects.all().values()
        return Response({'books': list(lst)})

#class BookList(generics.ListAPIView):
  #  queryset = Book.objects.all()
  #  serializer_class = BookSerializer

#lass BookDetail(generics.RetrieveUpdateDestroyAPIView):
 #   queryset = Book.objects.all()
  #  serializer_class = BookSerializer


class Reviewbook(APIView):
    def post(self, request):
        new_review = Review.objects.create(
            rating=request.data['rating'],
            text=request.data['text']
        )

        return Response({'review': model_to_dict(new_review)})