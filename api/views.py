from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from app.models import Aluno, Ficha_fisica
from .serializer import MySerializer
from .calculos.evolucao_fisica import CalculadorEvolucaoFisica
from .calculos.get_medidas import GetMedidas

# Create your views here.
@login_required
def api(request, pk, param):
    param_direito = None
    param_esquerdo = None
    param_unico = None
    qtd_de_avaliacoes = int(request.GET.get('filter'))
    if param == 'medida_antebraco' or param == 'medida_triceps' or param == 'medida_biceps':
        query_list = MySerializer().serialize(
                                    Ficha_fisica.objects.filter(aluno_id=pk).order_by('-created_at')[:qtd_de_avaliacoes],
                                    fields=['created_at', '{}_direito'.format(param), '{}_esquerdo'.format(param)])
        param_direito = True

    elif param == 'medida_coxa' or param == 'medida_panturrilha':
        query_list = MySerializer().serialize(
                                    Ficha_fisica.objects.filter(aluno_id=pk).order_by('-created_at')[:qtd_de_avaliacoes],
                                    fields=['created_at', '{}_direita'.format(param), '{}_esquerda'.format(param)])
        param_esquerdo = True
    
    elif param == 'medida_peito' or param == 'medida_abdomen' or param == 'medida_costas':
        query_list = MySerializer().serialize(
                                    Ficha_fisica.objects.filter(aluno_id=pk).order_by('-created_at')[:qtd_de_avaliacoes],
                                    fields=['created_at', '{}'.format(param)])
        param_unico = True

    medidas = []

    for item in query_list:
        medidas.append(item['fields'])
    
    if len(medidas) >=2:    
        if param_direito == True:
            print('param direito')    
            result_get_medidas = GetMedidas().get_medidas_direita(medidas, param)
            medidas.append(result_get_medidas)
        elif param_esquerdo == True:
            result_get_medidas = GetMedidas().get_medidas_esquerda(medidas, param)
            medidas.append(result_get_medidas)
        elif param_unico == True:
            result_get_medidas = GetMedidas().get_medidas_unicas(medidas, param)
            medidas.append(result_get_medidas)

    return JsonResponse(medidas, safe=False)