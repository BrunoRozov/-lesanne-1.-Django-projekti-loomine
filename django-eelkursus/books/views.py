from django.shortcuts import render

def index(request):
    return render(request, 'books/index.html')

def about(request):
    return render(request, 'books/about.html')

def index(request):

    raamatud = [
        {
            'nimi': 'Harry Potter',
            'autor': 'J. K. Rowling',
            'saadaval': True
        },
        {
            'nimi': 'Väike prints',
            'autor': 'Antoine de Saint-Exupéry',
            'saadaval': False
        },
        {
            'nimi': 'Kevade',
            'autor': 'Oskar Luts',
            'saadaval': True
        },
        {
            'nimi': 'Tõde ja õigus',
            'autor': 'A. H. Tammsaare',
            'saadaval': False
        },
        {
            'nimi': 'Kalevipoeg',
            'autor': 'Friedrich Reinhold Kreutzwald',
            'saadaval': True
        } 
    ]

    context = {
        'raamatud': raamatud,
        'pealkiri': 'Minu raamatukogu'
    } 

    return render(request, 'books/index.html', context)