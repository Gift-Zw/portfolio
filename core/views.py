from django.shortcuts import render
from .models import Projects


def home_view(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'index.html', context)




