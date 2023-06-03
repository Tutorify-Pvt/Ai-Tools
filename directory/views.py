import ast

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import *


# Create your views here.
def list_directory(request):
    view_data = {
        'title': 'Home',
        'directory': Directory.objects.filter(active=True),
        'tags': Tag.objects.all(),
    }
    return render(request, 'directory/list_directory.html', view_data)


def get_directory(request, id):
    directory = Directory.objects.get(id=id, active=True)
    directory.features = ast.literal_eval(directory.features)
    view_data = {
        'title': directory.title,
        'directory': directory,
        'tags': directory.tag.all(),
        'types': directory.types.all(),
    }
    return render(request, 'directory/view_directory.html', view_data)

def get_tags(request, tag_id):
    tags = Tag.objects.get(id=tag_id)
    view_data = {
        'title': f'{tags.title} Directories',
        'directory': Directory.objects.filter(tag__id=tag_id),
        'tags': Tag.objects.all(),
        'types': Type.objects.all(),
    }
    return render(request, 'directory/list_directory.html', view_data)

def get_type(request, type_id):
    types = Type.objects.get(id=type_id)
    view_data = {
        'title': f'{types.title} Directories',
        'directory': Directory.objects.filter(types__id=type_id),
        'tags': Tag.objects.all(),
        'types': Type.objects.all(),
    }
    return render(request, 'directory/list_directory.html', view_data)






@login_required(login_url='login')
def review_directory(request):
    view_data = {
        'title': 'Review',
        'directory': Directory.objects.filter(active=None),
    }

    return render(request, 'directory/list_directory.html', view_data)

@login_required(login_url='login')
def create_directory(request):
    view_data = {
        'title': 'Create Directory',
        'form': Directory_form()
    }
    if request.method == 'POST':
        form = Directory_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('directory_view')

    return render(request, 'directory/create_directory.html', view_data)

@login_required(login_url='login')
def edit_directory(request,id):
    form_data = Directory.objects.get(id = id)
    view_data = {
        'title': f'Edit Directory {form_data.title}',
        'form': Directory_form(instance=form_data),
        'id': id,
    }
    if request.method == 'POST':
        form = Directory_form(request.POST, instance=form_data)

        if form.is_valid():
            form.save()
            return redirect('directory_view')

    return render(request, 'directory/edit_directory.html', view_data)

