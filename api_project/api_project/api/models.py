from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=150)
 #create another class
class student(models.Model):
    firstname=models.CharField(max_length=100) 
    lastname=models.CharField(max_length=150)  