from .models import Workout
from django import forms


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields =  ['title', 'content', 'length', 'participants', 'equipment']

form = WorkoutForm()

