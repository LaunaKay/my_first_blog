from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html', {'name': "Launa", 'interest': "Photography", 'language': "My favorite language is python!"})
