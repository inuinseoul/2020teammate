from django import forms
from .models import Team_list

class Team_form(forms.ModelForm):

    class Meta:
        model = Team_list
        fields = ('name', 'intro',)