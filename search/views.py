#coding: utf-8

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from posts.models import Post

def search(request, query):
    """
    searches posts with given as a param query
    """
    try:
        if(query == ''):
            query = request.GET['query']
        posts = Post.search.query(query)
        context = { 'posts': list(posts),'query': query, 'search_meta':posts._sphinx }
    except:
        context = { 'posts': list() }

    return render_to_response('search/search_results.html', context, context_instance=RequestContext(request))