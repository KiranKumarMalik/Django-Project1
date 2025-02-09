from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def welcomeblinkit(request):
    return HttpResponse('<h1>Welcome to Blinkit</h1>')

def blinkit(request):
    return render(request,'blinkit.html')