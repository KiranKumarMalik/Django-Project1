from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def kiran(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def sagar(request):
    return HttpResponse('Sagar is a Play Boy')

def hello(request):
    return HttpResponse("<h1>Hello Kiran</h1> \n <h2>Hello Sagar</h2> \n <h3>Hello Chiku</h3>")

def youtube(request):
    return HttpResponse("<h1> Watch Youtube Videos </h1>")

def form(request):
    return render(request, 'form.html')