#coding: utf-8

from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from points.models import Point,PointAddForm
import django.utils.simplejson as json

#index method for displaying
#all points on map
from providers.models import Provider

def index(request):
    return render_to_response('points/index.html',{})


#method for returning back json response with all points
def getAllPoints(request):
    if request.method == 'POST':
        try:
            if not len(request.POST['provider']):
                temp_output = serializers.serialize('python', Point.objects.all())
            else:
                filter_provider = Provider.objects.get(name = request.POST['provider'])
                temp_output = serializers.serialize('python',
                    Point.objects.filter(provider = filter_provider))
            output = json.dumps(temp_output, cls=DjangoJSONEncoder)
        except :
            return HttpResponse(json.dumps({'success' : 'no'}, cls=DjangoJSONEncoder),
                mimetype="application/json")
        return HttpResponse(output, mimetype="application/json")

def create(request):
    form = PointAddForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)
            return redirect('points.views.index')
    return render_to_response('points/create.html', {'form' : form})
