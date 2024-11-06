from django.db import models,connection,transaction
from shared import models as base_model,erros
from hotels import models as hotel_model

# Create your models here.

class HotelRooms(models.Model):
  type = models.TextField(max_length = 30)
  price = models.IntegerField()
  room_number = models.IntegerField()
  hotel = models.ForeignKey(hotel_model.Hotels,on_delete=models.CASCADE)
  class Meta:
    unique_together = ['hotel', 'room_number']
  @staticmethod
  def adding_rooms(rooms):
    query = """INSERT INTO hotelrooms_hotelrooms (type,price,room_number,hotel_id)
               VALUES (%s,%s,%s,%s);"""
    try:
      with transaction.atomic():
        with connection.cursor() as cursor:
          for room in rooms:
            params = (room['type'],room['price'],room['room_number'],room['hotel_id'])
            cursor.execute(query,params)
    except Exception as e:
      raise erros.DataBaseErrors.AddinRoomsError(f'There Seems to Be Some Kind of Error --> From adding_rooms {e}')
  @staticmethod
  def update_rooms(rooms):
      query = """ 
      UPDATE hotelrooms_hotelrooms
      SET type = %s,price = %s,room_number = %s
      WHERE id = %s AND hotel_id = %s;"""
      try:
        with transaction.atomic():
          with connection.cursor() as cursor:
            for room in rooms:
              params = (room['type'],room['price'],room['room_number'],room['id'],room['hotel_id'])
              cursor.execute(query,params)
      except Exception as e:
        raise erros.DataBaseErrors.UpdatingRoomsError(f'There Seems to Be Some Kind of Error --> From updating_rooms {e}')
  
        
    
