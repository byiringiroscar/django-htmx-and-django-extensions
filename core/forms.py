from django import forms



class FilmForm(forms.Form):
    name = forms.CharField(max_length=100)