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
    return JsonResponse({'error':f'method should be Post'},status=405)
@csrf_exempt
def updating_rooms(request):
  if request.method == "PUT":
    try:
      data = json.loads(request.body)
      HotelRooms.update_rooms(data['rooms'])
      return JsonResponse({'sucsefuly':'Rooms Has Been Updated'},status =204)
    except erros.DataBaseErrors.UpdatingRoomsError as updateError:
      return JsonResponse({'error':str(updateError)})
    except Exception as e:
      return JsonResponse({'error':f'there seems to be error --> views/update_rooms {str(e)} '},status=400)
  else:
    return JsonResponse({'error':f'method should be PUT'},status=405)
  