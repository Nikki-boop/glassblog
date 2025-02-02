from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm

def blog_view(request):
    posts = BlogPost.objects.all()
    return render(request, 'glassblog/blog.html', {'posts': posts})

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
