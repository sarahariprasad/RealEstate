from django.db import models

import datetime
# Create your models here.

project_type = (
    ('Previous', 'Previous'),
    ('Current', 'Current'),
    ('Upcoming', 'Upcoming')

)


class Property(models.Model):
    name = models.CharField(max_length=50)
    project = models.CharField(choices=project_type, max_length=50, default='')
    availability = models.BooleanField(default=False)
    location = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='property/', null=True)
    date = models.DateTimeField(default=datetime.datetime.today)

    def __str__(self):
        return self.name
