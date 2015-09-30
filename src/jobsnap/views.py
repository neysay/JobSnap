from django.shortcuts import render
#from django.http import HttpResponse
from .forms import SignUpForm

# Create your views here.

def home(request):
    
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        
    context = {"form": form , "description":"Jobs in a snap."}
    return render(request, "home.html", context)

def employee(request):
    
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        
    context = {"form": form, "description":"A new way to find jobs you'll love."}
    return render(request, "employee.html", context)

def employer(request):
    
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        
    context = {"form": form, "description":"A new way to find candidates you'll love."}
    return render(request, "employer.html", context)

