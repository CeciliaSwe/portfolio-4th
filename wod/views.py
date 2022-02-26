from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib import messages
from .models import Workout
from .forms import WorkoutForm


class WorkoutList(generic.ListView):
    """
    Workout summary
    """

    model = Workout
    queryset = Workout.objects.order_by("-created_on")
    template_name = "index.html"
    paginate_by = 9


class WorkoutAdd(View):
    """ View to allow adding of new posts """

    def get(self, request, *args, **kwargs):

        return render(request,
                      "add_item.html", {"workout_form": WorkoutForm()})

    def post(self, request, *args, **kwargs):

        add_workout = WorkoutForm(data=request.POST)
        if add_workout.is_valid():
            add_workout.instance.author = request.user
            add_workout.save()
            messages.add_message(
                request, messages.SUCCESS, "Workout successfully added!"
            )
            return redirect("/")
        else:
            add_workout = WorkoutForm()
            messages.add_message(
                request, messages.ERROR,
                "Something went wrong, please try again!"
            )

        return render(
            request,
            'add_item.html',
            {

                "workout_form": WorkoutForm()
            },
        )


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
                "form": form,
            },
        )


class WorkoutEdit(View):
    """ View to allow editing of existing posts """

    def get(self, request, id, *args, **kwargs):
        queryset = Workout.objects
        workout = get_object_or_404(queryset, id=id)

        return render(
            request,
            "edit_item.html", {"workout_form": WorkoutForm(instance=workout)}
        )

    def post(self, request, id, *args, **kwargs):
        queryset = Workout.objects
        workout = get_object_or_404(queryset, id=id)

        add_workout = WorkoutForm(data=request.POST, instance=workout)
        if add_workout.is_valid():
            add_workout.save()
            messages.add_message(
                request, messages.SUCCESS, "Workout successfully updated!"
            )
            print("saving")
            return redirect("/")
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Workout could not be updated, please try again",
            )


def delete_item(request, id, *args, **kwargs):
    """ View to delete workout """
    queryset = Workout.objects
    workout = get_object_or_404(queryset, id=id)

    if request.user == workout.author:
        workout.delete()
        messages.add_message(request,
                             messages.WARNING, "Workout successfully deleted!")

    return redirect("/")
