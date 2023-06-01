from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import *
import ast



# Create your views here.
def list_directory(request):
    view_data = {
        'title': 'Home',
        'directory': Directory.objects.filter(active=True)
    }
    return render(request, 'directory/list_directory.html', view_data)

def get_directory(request,id):
    directory = Directory.objects.get(id=id, active=True)
    directory.features = ast.literal_eval(directory.features)
    view_data = {
        'title': directory.title,
        'directory': directory,
    }
    return render(request, 'directory/view_directory.html', view_data)

@login_required(login_url='login')
def review_directory(request):
    view_data = {
        'title': 'Review',
        'directory': Directory.objects.filter(active=None)
    }
    return render(request, 'directory/list_directory.html', view_data)

@login_required(login_url='login')
def create_directory(request):
    pass