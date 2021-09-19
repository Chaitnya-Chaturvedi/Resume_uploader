from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from .models import CustomUser, Resume

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

JOB_CITY_CHOICES = [
    ('Pune', 'Pune'),
    ('Mumbai', 'Mumbai'),
    ('Banglore', 'Banglore'),
    ('Delhi', 'Delhi'),
    ('Varodra', 'Varodra'),
]


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(
        label='Preferred job Locations',
        choices=JOB_CITY_CHOICES,
        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Resume
        fields = [
            'id',
            'name',
            'dob',
            'gender',
            'locality',
            'city',
            'pin',
            'state',
            'mobile',
            'email',
            'job_city',
            'profile_image',
            'my_file']
        labels = {
            'name': 'Full Name',
            'dob': 'Date of Birth',
            'pin': 'Pincode',
            'mobile': 'Mobile Number',
            'email': 'Email ID',
            'job_city': 'Preffered Location',
            'profile_image': 'Profile Picture',
            'my_file': 'Resume Copy'}

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pin': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),



        }
