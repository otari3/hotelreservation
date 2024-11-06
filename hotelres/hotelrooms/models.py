from django.db import models
from shared import models as base_model,erros
from hotels import models as hotel_model

# Create your models here.

class HotelRooms(models.Model):
  type = models.TextField(max_length = 30)
  price = models.IntegerField()
  room_number = models.IntegerField()
  hotel_id = models.ForeignKey(hotel_model.Hotels,on_delete=models.CASCADE)
