from django.shortcuts import render

# Create your views here.

def addProject(request):
    return render(request, 'core/addProject.html')

def contact(request):
    return render(request, 'core/contact.html')

def dashboard(request):
    return render(request, 'core/dashboard.html')

def myProjects(request):
    return render(request, 'core/myProjects.html')