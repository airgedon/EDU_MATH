# Generated by Django 4.1.6 on 2023-02-10 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_rename_text_lesson_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="lesson",
            name="upload",
            field=models.FileField(
                default="SOME STRING", max_length=254, upload_to="media/"
            ),
        ),
    ]
