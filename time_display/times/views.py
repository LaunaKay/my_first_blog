from django.shortcuts import render
from datetime import datetime

def index(request):
    return render(request, 'times/index.html', {'now': datetime.now()})
