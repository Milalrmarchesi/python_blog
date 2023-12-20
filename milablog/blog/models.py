from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class CreatorInfo(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    project_description = models.TextField()

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField() 
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)