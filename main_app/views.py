from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('1 Timothy 4:8')

def about(request):
    return render(request, 'about.html')