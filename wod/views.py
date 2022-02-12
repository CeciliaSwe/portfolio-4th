from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Workout
from .forms import WorkoutForm

class WorkoutList(generic.ListView):
    """
    Workout summary
    """
    model = Workout
    queryset = Workout.objects.order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6



class WorkoutAdd(View):
    """ View to allow adding of new posts """
    def get(self, request, *args, **kwargs):

        return render(
            request,
            'add_item.html',
            {
                'workout_form': WorkoutForm()
            }
        )

    def post(self, request, *args, **kwargs):

        add_workout = WorkoutForm(data=request.POST)

        if add_workout.is_valid():
            add_workout.save()
            return redirect("/")


        return redirect('/')





class WorkoutFull(View):
    """
    Display full workout as separate page
    """

    model = Workout

    def get(self, request, slug, *args, **kwargs):
        """
        Get data from workoutmodel
        """
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


