from django.shortcuts import render
from .models import Book


def index(request):
    raamatud = Book.objects.all()

    context = {
        'raamatud': raamatud,
        'pealkiri': 'Minu raamatukogu'
    }

    return render(request, 'books/index.html', context)


def available(request):
    raamatud = Book.objects.filter(available=True)

    context = {
        'raamatud': raamatud,
        'pealkiri': 'Saadaval raamatud'
    }

    return render(request, 'books/index.html', context)


def about(request):
    return render(request, 'books/about.html')