from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class User(AbstractUser):
    name = models.TextField(max_length=30, unique=True)
    description = models.CharField(max_length=120, blank = True)
    quantity = models.IntegerField(
    default = 1,
    validators=[MaxValueValidator(100), MinValueValidator(0)]
     )



