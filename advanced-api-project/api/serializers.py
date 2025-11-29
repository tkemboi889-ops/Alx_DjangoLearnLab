from rest_framework import serializers
from datetime import datetime
from .models import Author, Book


# -------------------------------------------------------
# BookSerializer
# -------------------------------------------------------
# Serializes all fields of the Book model.
# Includes custom validation to ensure that
# publication_year is not in the future.
# -------------------------------------------------------
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom field-level validation
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


# -------------------------------------------------------
# AuthorSerializer
# -------------------------------------------------------
# Serializes the Author model and includes all related
# books using a nested BookSerializer. The related_name
# 'books' from the Book model makes this possible.
# -------------------------------------------------------
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serializer

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
