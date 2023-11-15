from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random


@csrf_exempt
def result(request):
    data = request.POST
    cadastre_number = data.get('cadastre_number')
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    external_response = random.choice(["True", "False"])

    response_data = {
        'cadastre_number': cadastre_number,
        'latitude': latitude,
        'longitude': longitude,
        'external_response': external_response
    }

    return JsonResponse(response_data)