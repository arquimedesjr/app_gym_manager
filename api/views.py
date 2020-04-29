from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from app.models import Aluno, Ficha_fisica
from .serializer import MySerializer

# Create your views here.
@login_required
def api(request, pk, param):
    aluno = list(Ficha_fisica.objects.filter(aluno_id=pk).values(param, 'created_at').order_by('-created_at'))[:5]
    date = Ficha_fisica.objects.filter(aluno_id=pk).values(param).dates('created_at', 'day')

    query_list = MySerializer().serialize(
                                Ficha_fisica.objects.filter(aluno_id=pk).order_by('-created_at')[:5],
                                fields=['created_at', f'{param}'])

    medidas = []

    for item in query_list:
        medidas.append(item['fields'])
        print(medidas)

    return JsonResponse(medidas, safe=False)