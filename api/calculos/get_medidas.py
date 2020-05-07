from .evolucao_fisica import CalculadorEvolucaoFisica

class GetMedidas():
    def get_medidas_direita(self, medidas, param):
        if len(medidas) >= 2:
            segunda_medida = medidas[1]
            primeira_medida = medidas[0]

            #Medida direita
            primeira_medida_direita = primeira_medida.get(f'{param}_direito')
            segunda_medida_direta = segunda_medida.get(f'{param}_direito')

            #Medida Esquerda
            primeira_medida_esquerda = primeira_medida.get(f'{param}_esquerdo')
            segunda_medida_esquerda = segunda_medida.get(f'{param}_esquerdo')

            musculo_direito = CalculadorEvolucaoFisica().evolucao_fisica(primeira_medida_direita, segunda_medida_direta)
            musculo_esquerdo = CalculadorEvolucaoFisica().evolucao_fisica(primeira_medida_esquerda, segunda_medida_esquerda)
            return { 'evolucao': {
                        'evolucao_musculo_direito': musculo_direito,
                        'evolucao_musculo_esquerdo': musculo_esquerdo
                        }
                  }

    def get_medidas_esquerda(self, medidas, param):
        if len(medidas) >= 2:
            segunda_medida = medidas[1]
            primeira_medida = medidas[0]

            #Medida direita
            primeira_medida_direita = primeira_medida.get(f'{param}_direita')
            segunda_medida_direta = segunda_medida.get(f'{param}_direita')

            #Medida Esquerda
            primeira_medida_esquerda = primeira_medida.get(f'{param}_esquerda')
            segunda_medida_esquerda = segunda_medida.get(f'{param}_esquerda')

            musculo_direito = CalculadorEvolucaoFisica().evolucao_fisica(primeira_medida_direita, segunda_medida_direta)
            musculo_esquerdo = CalculadorEvolucaoFisica().evolucao_fisica(primeira_medida_esquerda, segunda_medida_esquerda)
            return { 'evolucao': {
                        'evolucao_musculo_direito': musculo_direito,
                        'evolucao_musculo_esquerdo': musculo_esquerdo
                        }
                    }