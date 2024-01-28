from django.db import models

# Create your models here.


class Element(models.Model):
    name = models.CharField(max_length = 100)
    country = models.CharField(max_length = 50)
    email = models.EmailField()

    # def __str__(self):
    #     return self.name