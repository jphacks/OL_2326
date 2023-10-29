from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from .models import Recording

# Create your views here.

def record_template(request: HttpRequest):
    return render(request, 'training/record.html')

def handle_uploaded_file(f, file_id):
    with open(f'media/recordings/rec_{file_id}.webm', 'wb+') as dest:
        for chunk in f.chunks():
            dest.write(chunk)

@csrf_exempt
def upload_recording(request: HttpRequest):
    if request.method == 'POST' and request.FILES['audio']:
        tz_now = timezone.now()

        recording = Recording.objects.create(created_at=tz_now, score=-1)

        recorded_file = request.FILES['audio']
        handle_uploaded_file(recorded_file, recording.id)

        # 必要な他の処理を実行する
        return HttpResponse("Data received successfully")
    else:
        return HttpResponse("Data not received", status=400)
    
def result_template(request: HttpRequest):
    return render(request, 'training/result.html')