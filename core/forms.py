from django import forms



class FilmForm(forms.Form):
    name = forms.CharField(max_length=100)


    def clean_name(self):
        if self.cleaned_data.get('name').startswith('a'):
            raise forms.ValidationError('Name cannot start with a')