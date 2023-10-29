from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from .score import score
from .models import Recording

# Create your views here.

def record_template(request: HttpRequest):
    return render(request, 'training/record.html')

def handle_uploaded_file(f, recording_id):
    with open(f'/media/recordings/rec_{recording_id}.webm', 'wb+') as dest:
        for chunk in f.chunks():
            dest.write(chunk)

@csrf_exempt
def upload_recording(request: HttpRequest):
    if request.method == 'POST' and request.FILES['audio']:
        tz_now = timezone.now()

        recording = Recording.objects.create(created_at=tz_now, score=-1)

        recorded_file = request.FILES['audio']
        handle_uploaded_file(recorded_file, recording.id)

        # recording_score = score(None)
        # recording.score = recording_score
        
        recording.save()

        # 必要な他の処理を実行する
        # return HttpResponse("Data received successfully")
        # return redirect("training:result")
        return redirect(f"/training/result/?id={recording.id}")
    else:
        return HttpResponse("Data not received", status=400)
    
def get_scores(recording_id):
    recording = Recording.objects.filter(id=recording_id)
    return {
        'score': recording[0].score
    }
    
def result_template(request: HttpRequest):
    recording_id = -1
    if 'id' in request.GET:
        recording_id = request.GET['id']
        scores = get_scores(recording_id)
    
    # return HttpResponse(f"score: {scores['score']}")
    return render(request, 'training/result.html', context=scores)
