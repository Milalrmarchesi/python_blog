from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, CreatorInfo, Blog
from .forms import AuthorForm, CategoryForm, PostForm, SearchForm, BlogForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import datetime

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


def about(request):
    creator_info = CreatorInfo.objects.first()
    return render(request, 'blog/about.html', {'creator_info': creator_info})


def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blog_detail.html', {'blog': blog})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.date = datetime.now().date()
            blog.time = datetime.now().time()
            blog.save()
            return redirect('blog_list')
        else:
            print(form.errors)  # Imprime los errores de validación en la consola
    else:
        form = BlogForm()
    return render(request, 'blog/add_blog.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_list')  
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/edit_blog.html', {'form': form, 'blog': blog})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')  
    return render(request, 'blog/delete_blog.html', {'blog': blog})

def page_not_found(request, unknown_path):
    return render(request, 'blog/page_not_found.html', {'unknown_path': unknown_path})