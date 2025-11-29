from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.exceptions import ValidationError
from django_filters import rest_framework as filters

from .models import Book
from .serializers import BookSerializer

# -------------------------------
# List all books with filtering, searching, and ordering
# Anyone can read; authenticated users can write
# Filtering: title, author, publication_year
# Searching: title, author__name
# Ordering: title, publication_year
# -------------------------------
class BookListView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, and ordering
    filter_backends = [
        rest_framework.DjangoFilterBackend,  # filtering
        filters.SearchFilter,                # search
        filters.OrderingFilter               # ordering
    ]

    # Fields that can be filtered
    filterset_fields = ['title', 'author', 'publication_year']

    # Fields that can be searched
    search_fields = ['title', 'author__name']

    # Fields that can be used for ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering

    def get_queryset(self):
        return Book.objects.all()


# -------------------------------
# Retrieve single book by ID
# Anyone can read
# -------------------------------
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# -------------------------------
# Create a new book
# Only authenticated users
# Custom validation: publication_year cannot be in the future
# -------------------------------
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if serializer.validated_data['publication_year'] > 2025:
            raise ValidationError("Publication year cannot be in the future.")
        serializer.save()


# -------------------------------
# Update an existing book
# Only authenticated users
# Custom validation: publication_year cannot be in the future
# -------------------------------
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        if serializer.validated_data['publication_year'] > 2025:
            raise ValidationError("Publication year cannot be in the future.")
        serializer.save()


# -------------------------------
# Delete a book
# Only authenticated users
# -------------------------------
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

