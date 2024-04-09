from django.shortcuts import render
from django_htmx.http import HttpResponseLocation, HttpResponseStopPolling 
from django.http import HttpResponse
import random
# Create your views here.


def index(request):
    if request.htmx:
        # return HttpResponseLocation('/success/', target="#htmx-content")
        return render(request, 'partial.html')
    return render(request, 'index.html')


def success(request):
    if random.random( ) > 0.35:
        print("pooling temrinated ....")
        return HttpResponseStopPolling()
    return HttpResponse('Success always!')