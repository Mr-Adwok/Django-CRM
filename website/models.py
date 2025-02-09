from django.db import models

# Create your models here.
class Just(models.Model):
	name = models.CharField(max_length = 200 )