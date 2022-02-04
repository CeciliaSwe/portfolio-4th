from . import views
from django.urls import path

urlpatterns = [
    path("", views.WorkoutList.as_view(), name="home"),
    path('<slug:slug>/', views.WorkoutFull.as_view(), name='workout_full'),
]