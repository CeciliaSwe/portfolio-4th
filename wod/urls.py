from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.WorkoutList.as_view(), name="home"),
    path('add_item/', views.add_item, name='add_item'),
    path('<slug:slug>/', views.WorkoutFull.as_view(), name='workout_full'),


]