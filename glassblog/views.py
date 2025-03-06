from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm

def blog_view(request):
    posts = BlogPost.objects.all()
    topics = BlogPost.objects.values_list('topic', flat=True).distinct()
    context = {
        'posts': posts,
        'topics': topics,
    }
    return render(request, 'glassblog/blog.html', context)

@login_required
def submit_view(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = BlogPostForm()
    return render(request, 'glassblog/submit.html', {'form': form})

@login_required
def update_post_view(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'glassblog/submit.html', {'form': form})

@login_required
def delete_post_view(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('blog')
    return render(request, 'glassblog/delete_post.html', {'post': post})