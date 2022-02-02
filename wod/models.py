from django.db import models
from django.contrib.auth.models import User

WORKOUT_LENGTH_OPTIONS = (
    ("Short < 25mins", "Short < 25mins"),
    ("Medium 30-45mins", "Medium 30-45mins"),
    ("Long > 45mins", "Long > 45mins")
)


WORKOUT_CATEGORY_OPTIONS = (
    ("Strength", "Strength"),
    ("Endurance", "Endurance"),
    ("Technique", "Technique")
)

WORKOUT_PARTICIPANTS_OPTIONS = (
    ("Single", "Single"),
    ("Duo", "Duo"),
    ("Trio", "Trio")
)

WORKOUT_EQUIPMENT_OPTIONS = (
    ("Dumbbell", "Dumbbell"),
    ("Barbell", "Barbell"),
    ("Kettlebell", "Kettlebell"),
    ("Assault bike", "Assault bike"),
    ("Plyobox", "Plyobox"),
    ("Rig", "Rig"),
    ("Wallball", "Wallball"),
    ("Jumprope", "Jumprope"),
    ("Rope", "Rope"),
    ("Rower", "Rower"),
    ("SkiErg", "SkiErg")
)

class Workout(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workout_post"
    )
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=30, choices=WORKOUT_CATEGORY_OPTIONS)
    length = models.CharField(max_length=30, choices=WORKOUT_LENGTH_OPTIONS)
    participants = models.CharField(max_length=30, choices=WORKOUT_PARTICIPANTS_OPTIONS)
    equipment = models.CharField(max_length=30, choices=WORKOUT_EQUIPMENT_OPTIONS, default="Barbell")

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


