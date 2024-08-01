from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

def start(request):
    return HttpResponse('<h1> Get started page</h1>')

def sign(request):
    return HttpResponse('<h1> Sgin in page</h1>')

def home(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})

def search(request):
    return HttpResponse('<h1> Search page</h1>')

def profile(request):
    return HttpResponse('<h1> Profile page</h1>')