from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def welcomeswiggy(request):
    return HttpResponse('<h1>Welcome Swiggy</h1>')
def swiggy(request):
    return render(request,'swiggy.html')