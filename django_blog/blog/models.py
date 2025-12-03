from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create a post model.
class Post(models.Model):
    title= models.CharField(max_length=200)
    content= models.TextField()
    published_date= models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    

def __str__(self):
        return self.title
#implementing a comment functionality
class Comment(models.Model):
      post=models.ForeignKey(Post,on_delete=models.CASCADE)
      author=models.ForeignKey(User,on_delete=models.CASCADE)
      content=models.TextField(),
      created_at=models.DateTimeField(default=timezone.now)
      updated_at=models.DateTimeField(auto_now=True)
def __str__(self):
    return f"Comment by {self.author} on {self.post}"
#implementing tag model functionality
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
#modify post model
class Post(models.Model):
    # your existing fields...
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
