from django.db import models

# Create your models here.
class blogpost(models.Model):
    name = models.CharField(max_length=100)
    blog = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name