from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  
    search_fields = ('title', 'author')  
    list_filter = ('publication_year',)  

admin.site.register(Book, BookAdmin)

# Define the custom UserAdmin class
class CustomUserAdmin(UserAdmin):
    # Fields to include in the creation form in the admin
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo', 'email', 'first_name', 'last_name')}),
    )
    
    # Fields to display when editing a user
    # Add your custom fields to the user information fieldset
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo')}),
    )

    # Fields to display in the user list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_of_birth')
    
    # Fields that can be filtered on the user list view
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'date_of_birth')


# Register the CustomUser model with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)