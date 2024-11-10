from django.db import models
from shared import models as base_model,erros
from hotels.models import Hotels  

# Create your models here.

class User(models.Model):
  name = models.TextField()
  personal_id = models.IntegerField()
  hotel = models.ForeignKey(Hotels,on_delete=models.CASCADE)
  class Meta:
    unique_together = ('hotel', 'personal_id')
