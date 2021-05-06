from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),

    #PROFILES
    path('profiles/index/', views.profiles_index, name='profiles_index'),
    path('profiles/new/', views.new_profile, name='new_profile'),

    # WORKOUTS
    path('workouts/index/', views.workouts_index, name='index'),
    path('workouts/<int:workout_id>/', views.workouts_detail, name='detail'),

    path('accounts/signup', views.signup, name='signup'),
]
