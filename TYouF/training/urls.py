from django.urls import path

from . import views

urlpatterns = [
    path('record/', views.record_template, name='record'),
    path('record/upload_recording/', views.upload_recording, name='upload_recording'),
    path('result/', views.result_template, name='result'),
    # path('list/', views.record_template, name='top'),
]