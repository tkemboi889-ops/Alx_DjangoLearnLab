from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.conf import settings # Import settings
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
    
    class Meta:
        permissions = [
            ("can_add_book", "Can add a new book"),
            ("can_change_book", "Can edit a book"),
            ("can_delete_book", "Can delete a book"),
        ]
    
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
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices = ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()






class CustomUserManager(BaseUserManager):
   
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        
        # Note: We can remove 'username' requirement from AbstractUser here,
        # but for simplicity, we'll keep AbstractUser's existing fields.
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        
       


        if 'date_of_birth' not in extra_fields:
            
            
         if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        
        
        if 'username' not in extra_fields:
             extra_fields['username'] = email

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    
    
    objects = CustomUserManager() 

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    
    def __str__(self):
        return self.email or self.username
    
   

class book(models.Model):
    # Use settings.AUTH_USER_MODEL for the ForeignKey
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='books'
    )
    title = models.CharField(max_length=200)
    # ... other fields