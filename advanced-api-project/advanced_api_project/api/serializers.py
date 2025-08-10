from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for Book instances.
    Validates that publication_year is not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                f"publication_year ({value}) cannot be in the future (>{current_year})."
            )
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for Author instances.
    Includes nested BookSerializer for related books.
    The nested 'books' field is read-only (books created via Book endpoint).
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
