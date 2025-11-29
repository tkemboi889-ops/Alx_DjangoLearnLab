from django.db import models

# Create your models here.
from django.db import models


# -------------------------------------------------------
# Author Model
# -------------------------------------------------------
# Represents a book author. This model has a one-to-many
# relationship with the Book model (one Author → many Books).
# -------------------------------------------------------
class Author(models.Model):
    name = models.CharField(max_length=255)  # Author name

    def __str__(self):
        return self.name


# -------------------------------------------------------
# Book Model
# -------------------------------------------------------
# Represents a book written by an Author. Each Book is linked
# to one Author via a foreign key. This establishes a one-to-many
# relationship: one Author can have multiple Books.

class Book(models.Model):
    title = models.CharField(max_length=255)                # Title of the book
    publication_year = models.IntegerField()                # Year published
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'                                # Allows author.books.all()
    )

    def __str__(self):
        return self.title
