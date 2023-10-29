from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from .models import Recording


def watch_template(request: HttpRequest):
    context = {
        "recodings_list": [f"/media/recordings/rec_{x.id}.webm" for x in Recording.objects.all()],
    }
    return render(request, 'watch/watch.html', context=context)