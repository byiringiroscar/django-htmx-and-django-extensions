from django.shortcuts import render
from django_htmx.http import HttpResponseLocation, HttpResponseStopPolling 
from django.http import HttpResponse

# Create your views here.


def index(request):
    if request.htmx:
        return HttpResponseLocation('/success/', target="#htmx-content")
        # return render(request, 'partial.html')
    return render(request, 'index.html')


def success(request):
    return HttpResponse('Success always!')