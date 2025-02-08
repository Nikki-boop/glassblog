from django.shortcuts import render, redirect
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

def submit_view(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = BlogPostForm()
    return render(request, 'glassblog/submit.html', {'form': form})

# Create your views here.
