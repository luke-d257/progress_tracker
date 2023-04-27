from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import AddProject, EditProject
from .models import NewProject
# Create your views here.
@login_required
def addProject(request):
    return render(request, 'core/addProject.html')
@login_required
def contact(request):
    return render(request, 'core/contact.html')
@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')


def home(request):
    return render(request, 'core/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect ('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html',{"form":form})
    

@login_required
def newProject(request):
    if request.method == 'POST':
        form = AddProject(request.POST, request.FILES)
        if form.is_valid():
            projects = form.save(commit=False)
            projects.created_by = request.user
            projects.save()

            return redirect ('/myProjects/')
    else:
        form = AddProject()

    return render(request, "core/newProject.html", {
        "form":form
    })

@login_required
def myProjects(request):
    projects = NewProject.objects.all()
    return render(request, 'core/myProjects.html', {
        "projects":projects
    })

@login_required
def closer (request, pk):
    project = get_object_or_404(NewProject, pk=pk) 

    return render (request, "core/closer.html", {
        "project":project
    })

@login_required
def dashboard(request):
    projects = NewProject.objects.filter(created_by = request.user)
    return render(request,'core/dashboard.html', {
        "projects":projects
    })

@login_required
def delete(request, pk):
    project = get_object_or_404(NewProject, pk=pk, created_by = request.user)
    project.delete()

    return redirect('core:dashboard')

@login_required
def editProject(request, pk):
    project = get_object_or_404(NewProject, pk=pk, created_by = request.user)
    if request.method == 'POST':
        form = EditProject(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect ('/myProjects/')
    else:
        form = EditProject(instance=project)

    return render(request, "core/newProject.html", {
        "form":form
    })

@login_required
def log_out(request):
    logout(request)
    return redirect('/login/')
