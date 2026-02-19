from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Post

posts_data = [

]

def get_date(post):
    return post.get("date")

# Create your views here.

def index(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/index.html', {'posts': latest_posts})

def posts(request):
    posts_all = Post.objects.all()
    return render(request, 'blog/posts.html', {'posts': posts_all})

def post(request, slug):
    try:
        post_details = get_object_or_404(Post, slug=slug)
        return render(request, 'blog/post-info.html', {
            'post': post_details,
            'tags': post_details.tags.all(),
        })
    except:
        raise Http404()