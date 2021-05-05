from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('1 Timothy 4:8')

def about(request):
    return render(request, 'about.html')

#AUTHORIZATION
# def signup(request):
#     error_message = ''
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('new_profile')
