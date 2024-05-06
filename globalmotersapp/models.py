from django.db import models

# Create your models here.
class labours(models.Model):
    name = models.CharField(max_length = 20)
    dept = models.CharField(max_length = 20)
    regno = models.CharField(max_length = 20)
