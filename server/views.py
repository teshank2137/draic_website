from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'server/index.html')


def projects(request):
    return render(request, 'server/projects.html')


def contact(request):
    return render(request, 'server/contactus.html')


def achievements(request):
    return render(request, 'server/achievements.html')
