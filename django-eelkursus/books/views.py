from django.shortcuts import render

def index(request):
    return render(request, 'books/index.html')

def about(request):
    return render(request, 'books/about.html')