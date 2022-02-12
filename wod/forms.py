from django import forms
from .models import Workout


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['title', 'content', 'length', 'participants', 'equipment']
        widgets = {
            'equipment' : forms.RadioSelect(),
            'length' : forms.RadioSelect(),
            'participants' : forms.RadioSelect()

        }



