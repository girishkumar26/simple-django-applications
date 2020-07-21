from django.db import models


class Destination(models.Model):
    name = models.TextField(max_length=100)
    price = models.IntegerField
    desc = models.TextField(max_length=100)
    img = models.ImageField(upload_to='pics')
