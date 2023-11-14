from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Cadastre
import random
import threading
import time

def outside_server(cadastre_number, latitude, longitude):
    times_server = random.randint(1, 60)
    time.sleep(times_server)
    result = random.choice(["True", "False"])
    return result

@csrf_exempt
def query(request):
    if request.method == 'POST':
        data = request.POST
        cadastre_number = data.get('cadastre_number')
        latitude = data.get('latitude')
        longitude = data.get('longitude')


        if cadastre_number is None or latitude is None or longitude is None:
            return JsonResponse({'error': 'Missing required data'})

        result = outside_server(cadastre_number, latitude, longitude)
        try:
            cadastre = Cadastre.objects.create(
                cadastre_number=cadastre_number,
                latitude=latitude,
                longitude=longitude,
                external_response=result)
            return JsonResponse({'result': 'success'})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Invalid request method'})


@csrf_exempt
def result(request):
    if request.method == 'POST':
        data = request.POST
        query_id = data.get('query_id')
        result = data.get('result')
        cadastre = Cadastre.objects.get(pk=query_id)
        cadastre.external_response = result
        cadastre.save()

        return JsonResponse({'message': 'Успех'})
    else:
        return JsonResponse({'error': 'Ошибка'})

@csrf_exempt
def ping(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'Pong!'})
    else:
        return JsonResponse({'error': 'Server not answer'})


