from django import forms
from .models import Post,Tag
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import Comment

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

#creating a profile update form

class UpdateUserForm(UserChangeForm):
    password = None  # Hide password field

    class Meta:
        model = User
        fields = ["username", "email"]


#creating comment form
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3})
        }
#updating post forms for tags

from django import forms
from .models import Post, Tag

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Separate tags with commas")

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        post = super().save(commit=False)
        if commit:
            post.save()
        tag_names = [t.strip() for t in self.cleaned_data['tags'].split(',') if t.strip()]
        for tag_name in tag_names:
            tag, created = Tag.create_or_get(name=tag_name)
            post.tags.add(tag)
        return post
@classmethod
def create_or_get(cls, name):
    tag, created = cls.objects.get_or_create(name=name)
    return tag





class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  
