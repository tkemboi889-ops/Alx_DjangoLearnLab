from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
class Library(models.Model):
    name=models.CharField(max_length=130)
    books=models.ManyToManyField(Book)
    def __str__(self):
        return self.name
    
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




class UserProfile(models.Model):
  ROLE_ADMIN = 'Admin'
  ROLE_LIBRARIAN = 'Librarian'
  ROLE_MEMBER = 'Member'


  ROLE_CHOICES = [
   (ROLE_ADMIN, 'Admin'),
   (ROLE_LIBRARIAN, 'Librarian'),
   (ROLE_MEMBER,  'Member'),
]


user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
role = models.CharField(max_length=20, choices=ROLE_CHOICES , default= ROLE_MEMBER)


def __str__(self):
 return f"{self.user.username} ({self.role})"


# Signal to automatically create (and save) a UserProfile when a User is created
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
   if created:
    UserProfile.objects.create(user=instance)
   else:
# Ensure profile exists and stays in sync
    UserProfile.objects.get_or_create(user=instance)