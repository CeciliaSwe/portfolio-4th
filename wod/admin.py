from django.contrib import admin
from .models import Workout
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Workout)
class WorkoutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')

