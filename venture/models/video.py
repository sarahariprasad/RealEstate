from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=50)
    video = models.FileField(upload_to='property/', null=True)

    def __str__(self):
        return self.name


