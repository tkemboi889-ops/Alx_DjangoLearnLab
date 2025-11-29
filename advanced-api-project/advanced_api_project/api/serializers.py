from rest_framework import serializers
from .models import Book,Author
from datetime import datetime
class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=["name"]
      # Custom validation: publication year cannot be in the future
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value
    
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer to show all books for the author
    books = Bookserializer(many=True, read_only=True)

    class Meta:
        model =Author 
        fields = ['title','publication_year','name']
