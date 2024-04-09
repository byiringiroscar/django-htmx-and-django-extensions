from django.shortcuts import render
from django_htmx.http import HttpResponseLocation, HttpResponseStopPolling, push_url, reswap
from django.http import HttpResponse
import random
# Create your views here.


def index(request):
    if request.htmx:
        # return HttpResponseLocation('/success/', target="#htmx-content")
        # response = render(request, 'partial.html')
        # return push_url(response, '/lorem/')
        response  = render(request, 'partial.html')
        return reswap(response, 'beforeend')
    return render(request, 'index.html')


def success(request):
    if random.random( ) > 0.35:
        print("pooling temrinated ....")
        return HttpResponseStopPolling()
    return HttpResponse('Success always!')