from django.db import models
from PIL import Image
import os

def resizeImage(file_path):
    image = Image.open(file_path)
    desired_width = 600
    original_width, original_height = image.size
    aspect_ratio = original_width / original_height
    desired_height = int(desired_width / aspect_ratio)

    new_size = (desired_width, desired_height)
    resized_image = image.resize(new_size)

    resized_image.save(file_path, optimize=True, quality=75)

class Projects(models.Model):
    title = models.CharField(max_length=350)
    details = models.TextField(max_length=1000, default=None)
    url = models.URLField(default=None)
    image = models.ImageField(upload_to="app/media/images", default=None)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            # image_path = os.path.join("app/media/images", str(self.image))
            image_path = str(self.image)
            resizeImage(image_path)

class Expriences(models.Model):
    title=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    details=models.TextField(max_length=5000, default=None)
    startdate=models.DateField()
    enddate=models.DateField()

    def __str__(self):
        return self.title