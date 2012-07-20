#coding: utf-8

from django.core import serializers
from django.core.cache import cache
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.views.decorators.cache import cache_page
from points.models import Point,PointAddForm
import django.utils.simplejson as json
from providers.models import Provider

@cache_page(60 * 2)
def index(request):
    '''
    index method for displaying all points on map
    caching for 2 minutes
    '''
    return render_to_response('points/index.html',{})


def getAllPoints(request):
    '''
    method for returning back json response with all points to ajax request
    provider can be given in request to get all points hosted by given provider
    '''
    if request.method == 'POST':
        try:
            #trying to get from cache
            points = cache.get('points')
            if points == None:
                #if not fetching data from db and caching
                points = Point.objects.all()
                cache.set('points', points, 60 * 1)
            #if provider name is given in request returning all points belonging to it
            #if not returning all points
            if not len(request.POST['provider']):
                #serialinzing data from queryset to list type
                temp_output = serializers.serialize('python', points)
            else:
                filter_provider = Provider.objects.get(name = request.POST['provider'])
                temp_output = serializers.serialize('python',
                    points.filter(provider = filter_provider))
            #serializing as json using simplejson
            output = json.dumps(temp_output, cls=DjangoJSONEncoder)
        except :
            return HttpResponse(json.dumps({'success' : 'no'}, cls=DjangoJSONEncoder),
                mimetype="application/json")
        return HttpResponse(output, mimetype="application/json")



@cache_page(60 * 5)
def create(request):
    '''
    view method for adding new Point
    returns form if GET and validates and saves data if POST
    '''
    form = PointAddForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)
            return redirect('points.views.index')
    return render_to_response('points/create.html', {'form' : form})
