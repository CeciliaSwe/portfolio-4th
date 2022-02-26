from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path("", views.WorkoutList.as_view(), name="home"),
    path('add_item/', views.WorkoutAdd.as_view(), name='add_item'),
    path('edit_item/<int:id>/', views.WorkoutEdit.as_view(), name='edit_item'),
    path('delete_item/<int:id>/', views.delete_item, name='delete_item'),
    path('<slug:slug>/', views.WorkoutFull.as_view(), name='workout_full'),


]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
