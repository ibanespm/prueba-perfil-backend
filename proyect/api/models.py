from django.db import models
from django.core.validators import EmailValidator
# Create your models here.





class Element(models.Model):
    name = models.CharField(max_length = 100)
    country = models.CharField(max_length = 50)
    email = models.EmailField(validators=[EmailValidator()])

