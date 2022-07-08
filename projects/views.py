from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, template_name='projects/projects.html', context=context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    reviews = projectObj.review_set.all()
    context = {'project':projectObj, 'tags':tags, 'reviews':reviews}
    return render(request, template_name='projects/single-project.html', context=context)


# CRUD -> CREATE READ UPDATE DELETE

# CREATE
def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request, template_name='projects/project-form.html', context=context)

# UPDATE
