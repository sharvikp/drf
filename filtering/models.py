from django.db import models

# Create your models here.
class introduction(models.Model):                           # class model of introduction
    name = models.CharField(max_length=100)
    intro = models.CharField(max_length=100)
    video_link = models.CharField(max_length=100)

    def __str__(self):
        return self.name