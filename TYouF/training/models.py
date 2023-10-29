from django.db import models

# Create your models here.

class Recording(models.Model):
    created_at = models.DateTimeField()
    score = models.IntegerField(default=-1)
    # score_fluency = models.IntegerField()
    # score_vocab = models.IntegerField()
    # score = models.IntegerField()
    # score = models.IntegerField()