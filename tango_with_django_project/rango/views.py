from django.shortcuts import render

def index(request):
    return render(request, 'Rango says hey there world')
