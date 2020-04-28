from django.http import JsonResponse
from app.models import Aluno, Ficha_fisica
from .serializer import MySerializer

# Create your views here.

def api(request, pk, param):
    aluno = list(Ficha_fisica.objects.filter(aluno_id=pk).values(param, 'created_at').order_by('-created_at'))[:5]
    date = Ficha_fisica.objects.filter(aluno_id=pk).values(param).dates('created_at', 'day')

    query_list = MySerializer().serialize(
                                Ficha_fisica.objects.filter(aluno_id=pk).order_by('-created_at')[:5],
                                fields=['created_at', f'{param}'])

    for p in query_list:
        for item in p:
            print(f'P Fields: {item}')

            
    return JsonResponse(query_list, safe=False)