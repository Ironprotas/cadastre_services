from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Cadastre
import random
import time



import json

# ...

@csrf_exempt
def query(request):
    if request.method == 'POST':
        data = request.POST
        cadastre_number = data.get('cadastre_number')
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        if cadastre_number is None or latitude is None or longitude is None:
            return JsonResponse({'error': 'Missing required data'})

        times_server = random.randint(1, 2)
        time.sleep(times_server)

        # Вызываем функцию result для получения ответа
        answer = result(request)

        # Извлекаем все поля из ответа
        try:
            parsed_answer = json.loads(answer.content)
            cadastre_number_from_answer = parsed_answer.get('cadastre_number')
            latitude_from_answer = parsed_answer.get('latitude')
            longitude_from_answer = parsed_answer.get('longitude')
            external_response_from_answer = parsed_answer.get('external_response')

            # Ваш код для дальнейшей обработки полей

            # Сохраняем результат в БД
            cadastre = Cadastre.objects.create(
                cadastre_number=cadastre_number,
                latitude=latitude,
                longitude=longitude,
                external_response=external_response_from_answer
            )

            return JsonResponse({'result': 'success'})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Invalid request method'})



@csrf_exempt
def ping(request):
    if request.method == 'GET':
        external_url = "http://example.com"  # Используйте внешний URL для проверки доступности

        try:
            check_ping = requests.get(external_url)
            if check_ping.status_code == 200:
                return JsonResponse({'message': 'Pong!'})
            else:
                return JsonResponse({'error': 'Server not answering correctly'})

        except requests.RequestException as e:
            return JsonResponse({'error': 'Failed to connect to the external server'})

    else:
        return JsonResponse({'error': 'Invalid request method'})

