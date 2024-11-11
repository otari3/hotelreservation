import uuid
from django.db import models
from shared import models as base_model,erros
import jwt
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class Hotels(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  email = models.TextField(unique=True)
  password = models.TextField()
  name = models.TextField(unique=True)
  address = models.TextField()
  database_handeler = base_model.Data_base_handeler
  def register_hotel(self):
    query = """INSERT INTO hotels_hotels (name,address)
               VALUES (%s,%s);"""
    hashed_password = make_password(self.password)
    try:
      return self.database_handeler.execute_query(query,())
    except erros.DataBaseErrors.ExecuteQuery:
      raise
      
  @staticmethod
  def get_hotel(id):
    query = """ SELECT * FROM hotels_hotels 
                WHERE id = %s;"""
    try:
      return base_model.Data_base_handeler.select_one(query,(id,))
    except erros.DataBaseErrors.FormatingError:
      raise
    except erros.DataBaseErrors.SelectOneError:
      raise
  
  
    