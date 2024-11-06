from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import HotelRooms
from shared import erros

# Create your views here.
@csrf_exempt
def adding_rooms(request):
  if request.method == 'POST':
    try:
      data = json.loads(request.body)
      HotelRooms.adding_rooms(data['rooms'])
      return JsonResponse({'sucsefuly':'Rooms Has Been Added'},status=200)
    except erros.DataBaseErrors.AddinRoomsError as roomError:
      return JsonResponse({'error': str(roomError)},status=400)
    except Exception as e:
      return JsonResponse({'error':f'there seems to be error {str(e)}'},status=400)
  else:
    return JsonResponse({'error':f'method should be post'},status=405)