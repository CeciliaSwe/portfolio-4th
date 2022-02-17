from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms
from .models import Workout



class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['title', 'content', 'category', 'length', 'participants', 'equipment']
        widgets = {
            'equipment' : forms.RadioSelect(),
            'length' : forms.RadioSelect(),
            'participants' : forms.RadioSelect(),
            'category' : forms.RadioSelect(),
            'content': SummernoteWidget()
        }



