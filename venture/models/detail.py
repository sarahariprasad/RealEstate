from django.db import models
from .property import Property


class Detail(models.Model):
    name = models.CharField(max_length=50)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, default=None)
    address = models.CharField(max_length=500, default='')
    total_plots = models.CharField(max_length=50, default='')
    plots_sold_out = models.CharField(max_length=50, default='')
    plots_available = models.CharField(max_length=50, default='')
    total_area = models.CharField(max_length=50, default='')
    open_space = models.CharField(max_length=50, default='')
    utility = models.CharField(max_length=50, default='')
    amenities = models.CharField(max_length=50, default='')
    roads = models.CharField(max_length=50, default='')
    plotted = models.CharField(max_length=50, default='')
    mortgage = models.CharField(max_length=50, default='')
    characteristics = models.TextField(max_length=65535, default='')
    speciality = models.TextField(max_length=65535, default='')
    image = models.ImageField(upload_to='property', null=True)


