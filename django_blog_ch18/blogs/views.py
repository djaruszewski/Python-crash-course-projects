from django.shortcuts import render, redirect

from .models import BlogPost
from .forms import BlogPostForm
# Create your views here.

def index(request):
    """Home page for Blog."""
    titles = BlogPost.objects.order_by('date_added')
    context = {'titles': titles}
    return render(request, 'blogs/index.html', context)

def new_post(request):
    """Add new blog post."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogPostForm()
    else:
        # POST data submitted; process data.
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

def edit_post(request):
    """Edit an existing blog post."""
    post = BlogPost.objects.get(id=post_id)
    text = post.text
    title = post.title

    if request.method != 'POST':
        # Initial request; prefill form with current entry.
        form = BlogPostForm(instance=post)
    else:
        # POST data submitted; process data.
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index', post_id=post_id)

    context = {'form': form, 'post': post}
    return render(request, 'blogs/edit_post.html', context)