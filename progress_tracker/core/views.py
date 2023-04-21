from django.shortcuts import render, redirect

from .forms import SignupForm
# Create your views here.

def addProject(request):
    return render(request, 'core/addProject.html')

def contact(request):
    return render(request, 'core/contact.html')

def dashboard(request):
    return render(request, 'core/dashboard.html')

def myProjects(request):
    return render(request, 'core/myProjects.html')

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
    
  