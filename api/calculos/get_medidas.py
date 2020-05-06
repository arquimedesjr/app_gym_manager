from .evolucao_fisica import evolucao_fisica


def get_medidas(medidas, param):
    if len(medidas) >= 2:
        segunda_medida = medidas[1]
        primeira_medida = medidas[0]

        #Medida direita
        primeira_medida_direita = primeira_medida.get(f'{param}_direito')
        segunda_medida_direta = segunda_medida.get(f'{param}_direito')

        #Medida Esquerda
        primeira_medida_esquerda = primeira_medida.get(f'{param}_esquerdo')
        segunda_medida_esquerda = segunda_medida.get(f'{param}_esquerdo')

        musculo_direito = evolucao_fisica(primeira_medida_direita, segunda_medida_direta)
        musculo_esquerdo = evolucao_fisica(primeira_medida_esquerda, segunda_medida_esquerda)
        return {
                'evolucao_musculo_direito': musculo_direito,
                'evolucao_musculo_esquerdo': musculo_esquerdo
                }
    
    # if len(medidas) == 1:
    #     print('true')
    #     primeira_medida = medidas[0]
    #     primeira_medida_direita = primeira_medida.get(f'{param}_direito')
    #     primeira_medida_esquerda = primeira_medida.get(f'{param}_esquerdo')
    #     evolucao1 = evolucao_fisica(primeira_medida_direita, primeira_medida_esquerda)
    #     medidas.append({'evolucao1': evolucao1})
    #     return JsonResponse(medidas, safe=False)