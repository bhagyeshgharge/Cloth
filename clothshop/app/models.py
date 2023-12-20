from django.db import models

# Create your models here.
class Cloth(models.Model):
    product=models.CharField(max_length=60)
    # type=models.CharField(max_length=60)
    size=models.CharField(max_length=60)
    price=models.CharField(max_length=60)