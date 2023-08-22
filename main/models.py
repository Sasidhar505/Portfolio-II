from django.db import models

# Create your models here.

class Ma_Works(models.Model):
    proj_name = models.CharField(max_length=100)
    proj_img = models.ImageField(upload_to='images/')
    proj_link = models.CharField(max_length=200)
    proj_desp = models.TextField()

    def __str__(self):
        return self.proj_name