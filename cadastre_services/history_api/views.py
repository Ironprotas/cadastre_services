# history_api/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from cadastre.models import  Cadastre

@csrf_exempt
def history_by_cadastre(request, cadastre_number):
    if request.method == 'GET':
        try:
            history = Cadastre.objects.filter(cadastre_number=cadastre_number).values()
            history_list = list(history)
            return JsonResponse({'history': history_list})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Invalid request method'})
