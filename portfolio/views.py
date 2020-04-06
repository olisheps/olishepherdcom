from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/HTML/index.html')
