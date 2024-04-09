from django.shortcuts import render
from django_htmx.http import HttpResponseClientRedirect

# Create your views here.


def index(request):
    if request.htmx:
        return HttpResponseClientRedirect('/admin')
        # return render(request, 'partial.html')
    return render(request, 'index.html')