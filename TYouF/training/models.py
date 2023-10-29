from django.db import models

# Create your models here.

class Recording(models.Model):
    created_at = models.DateTimeField()
    score = models.IntegerField()