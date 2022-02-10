from django.shortcuts import render, get_object_or_404, reverse
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



def add_item(request):
    """
    Display the WorkoutForm in the add_item template
    """
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WorkoutForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect('index.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = WorkoutForm()

    return render(request, 'add_item.html', {'form': form})




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


