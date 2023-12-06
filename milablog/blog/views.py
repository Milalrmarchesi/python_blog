from django.shortcuts import render, redirect
from .models import Post
from .forms import AuthorForm, CategoryForm, PostForm, SearchForm
from django.db.models import Q

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})

def search_posts(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            results = Post.objects.filter(
                Q(title__icontains=search_query) | Q(content__icontains=search_query)
            )
            return render(request, 'blog/search_results.html', {'results': results, 'query': search_query})
    else:
        form = SearchForm()
    return render(request, 'blog/search_form.html', {'form': form})