from django.db import models

# Create your models here.
class Projects(models.Model):
    title=models.CharField(max_length=350)
    details=models.CharField(max_length=1000, default=None)
    url=models.URLField(default=None)
    image=models.ImageField(upload_to="app/media/images",default=None)

    def __str__(self):
        return self.title

class Expriences(models.Model):
    title=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    details=models.TextField(max_length=5000, default=None)
    startdate=models.DateField()
    enddate=models.DateField()

    def __str__(self):
        return self.title