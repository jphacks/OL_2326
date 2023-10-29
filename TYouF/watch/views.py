from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from ..training.models import Recording

# Create your views here.

def watch(request: HttpRequest):
    context = {
        "recordings_list": [f"rec_{x.id}.webm" for x in Recording.objects.all()]
    }
    return render(request, 'watch/watch.html', context=context)