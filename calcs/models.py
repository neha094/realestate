from django.db import models
from datetime import datetime


class Calc(models.Model):
    listing = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    Required = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    calc_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name




from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
