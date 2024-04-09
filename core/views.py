from django.shortcuts import render
from django_htmx.http import HttpResponseLocation, HttpResponseStopPolling, push_url, reswap, retarget, trigger_client_event
from django.http import HttpResponse
import random
from core.forms import FilmForm
# Create your views here.


def index(request):
    if request.htmx:
        form = FilmForm(request.GET)
        if form.is_valid():
            response = HttpResponse("Successfully submitted form!")
            return (response, 'film-added')
        context = {
            'form': form
        }
        response = render(request, 'form.html', context)
        return retarget(response, '#page-content')
        # return HttpResponseL
        # ocation('/success/', target="#htmx-content")
        # response = render(request, 'partial.html')
        # return push_url(response, '/lorem/')
        # response  = render(request, 'partial.html')
        # return reswap(response, 'beforeend')
    context = {
        'form': FilmForm()
    }
    return render(request, 'index.html', context)


def success(request):
    if random.random( ) > 0.35:
        print("pooling temrinated ....")
        return HttpResponseStopPolling()
    return HttpResponse('Success always!')trigger_client_event