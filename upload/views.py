from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from .forms import PhotoForm
from .models import Photo


def basicUploadFile(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {
                'is_valid': True,
                'name': photo.file.name,
                'url': photo.file.url
            }
        else:
            data = {
                'is_valid': False
            }
            print(data)
        return JsonResponse(data)
    context = {
        'photos': photos
    }
    return render(request, 'upload/basic_upload.html', context)


class BasicFileUploadView(View):
    def get(self, request):
        photos = Photo.objects.all()
        context = {
            'photos': photos,
        }
        return render(request, 'upload/basic_upload.html', context)

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {
                'is_valid': True,
                'name': photo.file.name,
                'url': photo.file.url
            }
        else:
            data = {
                'is_valid': False
            }

        print(data)
        return JsonResponse(data)
