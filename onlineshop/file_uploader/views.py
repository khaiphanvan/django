from django.shortcuts import render
from django.db import models

# Create your models here.
from django.http import HttpResponse
from .form import UploadFileForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def fileUploaderView(request):
    if request.method=='POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            upload(request.FILES['file'])
            return HttpResponse("<h2>File uploaded successful !</h2>")
        else:
            return HttpResponse("<h2>File uploaded not successful !</h2>")

    form = UploadFileForm()
    return  render(request, 'fileUploaderTemplate.html',{'form':form})


def upload(f):
    #path = default_storage.save('/file_upload', ContentFile('new content'))
    file = open(f.name,'wb+')
    for chunk in f.chunks():
        file.write(chunk)