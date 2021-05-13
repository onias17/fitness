from django import forms
from .models import Profile

class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'firstname', 'lastname', 'nickname', 'age' ]
