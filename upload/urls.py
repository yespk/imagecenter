from django.urls import path

from .views import BasicFileUploadView, basicUploadFile

app_name = 'upload'
urlpatterns = [
    path('basic_upload', basicUploadFile, name='basic-upload'),
]
