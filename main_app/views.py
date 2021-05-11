from django.shortcuts import render, redirect
from .models import Profile, Workout, Exercise
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# PROFILES
def profiles_index(request):
    profile = Profile.objects.get(user = request.user)

    return render(request, 'profiles/index.html')

def new_profile(request):
    if request.method == 'POST':
        profile_form = ProfileCreationForm(request.POST, request.FILES)


# WORKOUTS
def workouts_index(request):
    workouts = Workout.objects.all()
    return render(request, 'workouts/index.html', {'workouts': workouts})

def workouts_detail(request, workout_id):
    workout = Workout.objects.get(id=workout_id)
    return render(request, 'workouts/detail.html', {'workout': workout})

# AUTHORIZATION
def signup(request):
    error_message = ''

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('new_profile')
        else: 
            error_message = 'Invalid sign up - try again'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
    
