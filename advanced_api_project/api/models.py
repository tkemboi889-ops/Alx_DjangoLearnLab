from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
   #creates relationship between a book and author model 
class Book(models.Model):
    title=models.CharField(max_length=100)
    publication_year=models.IntegerField()
    Author=models.OneToOneField(Author,on_delete=models.CASCADE)
    def __str__(self):
        return self.titl
    