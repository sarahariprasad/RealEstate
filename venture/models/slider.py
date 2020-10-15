from django.db import models


class Slider(models.Model):
    name = models.CharField(max_length=50, default='')
    image = models.ImageField(upload_to='property/', null=True)

    def __str__(self):
        return self.name