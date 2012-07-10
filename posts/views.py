from django.shortcuts import render_to_response, get_object_or_404
from posts.models import Post

def index(request):
    posts = Post.objects.all().order_by('created_at')
    return render_to_response('posts/index.html', {'posts' : posts})

def details(request, post_id):
    post = get_object_or_404(Post,pk=post_id)
    return render_to_response('posts/details.html',{'post' : post})
