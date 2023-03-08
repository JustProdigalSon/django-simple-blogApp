from django.shortcuts import render, redirect
from django.http import HttpResponse
from.forms import commentForm
from .models import Post

def temp(request):
    return render(request, 'blog/temp.html')
    

def frontpage(request):
    posts = Post.objects.all()
    user = Post.user
    return render(request, 'blog/frontpage.html', {'posts': posts,'user': user})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
        return redirect('post_detail', slug=post.slug)    
    else:
        form = commentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})

