from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    #PROFILES
    path('profiles/index/', views.profiles_index, name='profiles_index'),
    path('profiles/new/', views.new_profile, name='new_profile'),
    path('profiles/<int:profile_id>/', views.profile_detail, name='detail'),
    path('profiles/<int:profile_id>/edit/', views.edit_profile, name='edit_profile'),
    # path('profiles/<int:profile_id>/delete/', views.delete_profile, name='delete_cat'),

    # WORKOUTS
    path('workouts/index/', views.workouts_index, name='workouts_index'),
    path('workouts/<int:workout_id>/', views.workouts_detail, name='detail'),

    path('accounts/signup', views.signup, name='signup'),
]
