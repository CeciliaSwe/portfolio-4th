from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Workout
from .forms import WorkoutForm

class WorkoutList(generic.ListView):
    model = Workout
    queryset = Workout.objects.order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6



class WorkoutFull(View):

    model = Workout

    def get(self, request, slug, *args, **kwargs):
        queryset = Workout.objects.order_by("-created_on")
        workout = get_object_or_404(queryset, slug=slug)
        form = WorkoutForm()


        return render(
            request,
            "workout_full.html",
            {
                "workout": workout,
                'form': form,
            },
        )
