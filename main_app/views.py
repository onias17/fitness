from django.shortcuts import render, redirect
from .models import Profile, Workout, Exercise
from .forms import ProfileCreationForm
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
    context = {'profile', profile}

    return render(request, 'profiles/index.html', context)

def new_profile(request):
    if request.method == 'POST':
        profile_form = ProfileCreationForm(request.POST, request.FILES)
        if profile_form.is_valid():
            new_profile = profile_form.save(commit=False)
            new_profile.user = request.user
            new_profile.save()

            return redirect('detail', new_profile)

    else:
        profile_form = ProfileCreationForm()
        context = {'profile_form' : profile_form}
        return render(request, 'profiles/new.html', context)

def profile_detail(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    context = {'profile' : profile}
    
    return render(request, 'profiles/detail.html', context)

@login_required
def edit_profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)

    if request.method == 'POST':
        profile_form = ProfileCreationForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            updated_profile = profile.form.save()
            return redirect('detail', updated_profile.id)
    
    else:
        profile_form = ProfileCreationForm(instance=profile)
        context = {'profiel_form' : profile_form }
        return render(request, 'profiles/edit.html', context)

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
    
