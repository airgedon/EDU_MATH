from django.db import models


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    upload = models.FileField(upload_to='media/', max_length=254, default='MEDIA')

    def __str__(self):
        return self.title

