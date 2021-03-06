from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project, Profile, Rating
from pyuploadcare.dj.models import ImageField

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProjectForm(forms.ModelForm):
    image = ImageField(blank=True, manual_crop="")

    class Meta:
        model = Project
        fields = ('image', 'title', 'url', 'description','technologies')


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'location', 'profile_image', 'bio', 'contact']


class RatingsForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['design','usability', 'content']