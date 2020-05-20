from django.db import models
from PIL import Image
class Destinations(models.Model):
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    def __str__(self):
        return self.name

