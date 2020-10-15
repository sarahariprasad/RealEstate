from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50, default='')
    email = models.EmailField()
    number = models.CharField(max_length=50, default='')
    text = models.TextField(max_length=1000, default='')

    def __str__(self):
        return self.name


