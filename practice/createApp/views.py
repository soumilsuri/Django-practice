from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("new app home page")

def new(request):
    return render(request, "createApp/new.html")
