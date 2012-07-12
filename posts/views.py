from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from posts.models import Post

def index(request):
    posts = Post.objects.all().order_by('created_at')
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render_to_response('posts/index.html', {'posts' : posts})

def details(request, post_id):
    post = get_object_or_404(Post,pk=post_id)
    return render_to_response('posts/details.html',{'post' : post})
