from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from app.models import Aluno, Ficha_fisica
from .serializer import MySerializer
from .calculos.evolucao_fisica import evolucao_fisica
from .calculos.get_medidas import get_medidas

# Create your views here.
@login_required
def api(request, pk, param):
    if param == 'medida_antebraco' or param == 'medida_triceps' or param == 'medida_biceps':
        query_list = MySerializer().serialize(
                                    Ficha_fisica.objects.filter(aluno_id=pk).order_by('-created_at')[:5],
                                    fields=['created_at', '{}_direito'.format(param), '{}_esquerdo'.format(param)])
        param_direito = True

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
    
    # if param_direito == True:
    #     print('param direito')    
    #     result_get_medidas = get_medidas(medidas, param)
    #     medidas.append(result_get_medidas)

    return JsonResponse(medidas, safe=False)