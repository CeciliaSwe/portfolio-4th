from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.WorkoutList.as_view(), name="home"),
    path('add_item/', views.WorkoutAdd.as_view(), name='add_item'),
    # path('edit_item/', views.WorkoutEdit.as_view(), name='edit_item'),
    path('<slug:slug>/', views.WorkoutFull.as_view(), name='workout_full'),


]