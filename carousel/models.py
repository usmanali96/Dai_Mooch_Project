from django.db import models

class Carousel(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    image = models.FileField(max_length=60, upload_to="products/", null=True)

# Create your models here.
