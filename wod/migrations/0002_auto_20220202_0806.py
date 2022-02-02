# Generated by Django 3.2 on 2022-02-02 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wod', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='favorite',
        ),
        migrations.AddField(
            model_name='workout',
            name='equipment',
            field=models.CharField(choices=[('Dumbbell', 'Dumbbell'), ('Barbell', 'Barbell'), ('Kettlebell', 'Kettlebell'), ('Assault bike', 'Assault bike'), ('Plyobox', 'Plyobox'), ('Rig', 'Rig'), ('Wallball', 'Wallball'), ('Jumprope', 'Jumprope'), ('Rope', 'Rope'), ('Rower', 'Rower'), ('SkiErg', 'SkiErg')], default='Barbell', max_length=30),
        ),
        migrations.AlterField(
            model_name='workout',
            name='length',
            field=models.CharField(choices=[('Short < 25mins', 'Short < 25mins'), ('Medium 30-45mins', 'Medium 30-45mins'), ('Long > 45mins', 'Long > 45mins')], max_length=30),
        ),
    ]