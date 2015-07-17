from django.shortcuts import render
from django.http import HttpResponse, Http404

def ninja (request):
    return render(request, 'ninja/ninja.html', {})

def color (request, color):
    if color == ('blue' or 'red' or 'orange'  or 'purple'):
        return render(request, 'ninja/color.html', {'color':color})
    else:
        return render('ninja/color.html', {'color':notapril})
