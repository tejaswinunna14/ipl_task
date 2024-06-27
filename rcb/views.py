from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def kingkohli(request):
    return HttpResponse('<h1>kohli is the best</h1>')