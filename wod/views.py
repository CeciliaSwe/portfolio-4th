from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Workout

class PostWorkout(generic.ListView):
    model = Workout()
    queryset = Workout.objects.order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6