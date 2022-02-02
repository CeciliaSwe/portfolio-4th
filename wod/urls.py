from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostWorkout.as_view(), name="home"),
]