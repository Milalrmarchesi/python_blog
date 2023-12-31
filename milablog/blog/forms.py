from django import forms
from .models import Author, Category, Post

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'category']
        
class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, label='Search')