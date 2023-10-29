from django.urls import path

from . import views_train, views_watch

app_name = 'training'
urlpatterns = [
    path('record/', views_train.record_template, name='record'),
    path('record/upload_recording/', views_train.upload_recording, name='upload_recording'),
    path('result/', views_train.result_template, name='result'),
    # path('list/', views.record_template, name='top'),
    path('watch/', views_watch.watch_template, name='watch'),
]