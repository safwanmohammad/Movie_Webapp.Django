from django import forms
from .models import Movie


class Movie_Form(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'img', 'year', 'price', 'desc']
