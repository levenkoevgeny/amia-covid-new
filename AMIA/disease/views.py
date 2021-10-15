from django.shortcuts import render
from .models import Disease


def index(request):
    diseases_list = Disease.objects.all()[:10]
    return render(request, 'disease/disease_main.html', {
        'disease_list': diseases_list
    })


def disease_list(request):
    diseases_list = Disease.objects.all()
    return render(request, 'disease/disease_main.html', {
        'disease_list': diseases_list
    })
