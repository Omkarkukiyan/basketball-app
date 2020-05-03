from django import forms

from .models import Players

class PlayerForm(forms.ModelForm):
    name = forms.CharField(max_length=50) 
    profile_pic = forms.ImageField()
    position = forms.CharField(max_length=50)
    country = forms.CharField(max_length=50)
    joined_date = forms.DateTimeField()

    class Meta:
        model = Players
        fields = "__all__"

