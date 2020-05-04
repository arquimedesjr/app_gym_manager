from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from app.models import Aluno, Ficha_fisica
from .serializer import MySerializer

# Create your views here.
@login_required
def api(request, pk, param):
    print(f'Params: {param}')
    if param == 'medida_antebraco' or param == 'medida_triceps' or param == 'medida_biceps':
        query_list = MySerializer().serialize(
                                    Ficha_fisica.objects.filter(aluno_id=pk).order_by('-created_at')[:5],
                                    fields=['created_at', '{}_direito'.format(param), '{}_esquerdo'.format(param)])

    elif param == 'medida_coxa' or param == 'medida_panturrilha':
        query_list = MySerializer().serialize(
                                    Ficha_fisica.objects.filter(aluno_id=pk).order_by('-created_at')[:5],
                                    fields=['created_at', '{}_direita'.format(param), '{}_esquerda'.format(param)])
    
    elif param == 'medida_peito' or param == 'medida_abdomen' or param == 'medida_costas':
        query_list = MySerializer().serialize(
                                    Ficha_fisica.objects.filter(aluno_id=pk).order_by('-created_at')[:5],
                                    fields=['created_at', '{}'.format(param)])

    medidas = []

    for item in query_list:
        medidas.append(item['fields'])
        print(medidas)

    return JsonResponse(medidas, safe=False)