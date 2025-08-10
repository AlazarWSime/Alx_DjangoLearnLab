from django.shortcuts import render
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import viewsets


class AuthorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Author model.
    Provides CRUD operations for Author instances.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Book model.
    Provides CRUD operations for Book instances.
    """
    queryset = Book.objects.select_related('author').all() # Using select_related to optimize queries
    # This will reduce the number of queries when accessing author data in BookSerializer 
    # by fetching related Author objects in a single query.
    # This is useful when you want to access author data in the BookSerializer.
    serializer_class = BookSerializer




# Create your views here.
