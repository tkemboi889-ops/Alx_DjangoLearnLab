from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings # Import settings
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Book(models.Model):
    title=models.CharField (max_length =200)
    author=models.CharField (max_length =100)
    publication_year= models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author}" 
    
    
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
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        
        
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
