from django.urls import path

from . import views

app_name = 'watch'
urlpatterns = [
    path('', views.watch, name='watch'),
]