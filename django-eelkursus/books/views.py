from django.shortcuts import render
from .models import Book

def index(request):
    return render(request, 'books/index.html')

def about(request):
    return render(request, 'books/about.html')

def index(request):
    raamatud = Book.objects.all()

    context = {
        'raamatud': raamatud,
        'pealkiri': 'Minu raamatukogu'
    } 

    return render(request, 'books/index.html', context)