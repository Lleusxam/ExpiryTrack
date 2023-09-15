from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    image_url = models.CharField(max_length=2083) #2083 is the max length of a url

    def __str__(self):
        return self.name