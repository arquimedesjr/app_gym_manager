import unittest
import hashlib

def classifica_percentul_gordura(sexo, idade, percentual_gordura):

  ## HOMENS COM IDADE ENTRE 18 ANOS E 25 ANOS DE IDADE 
  if (sexo == 'M') and (idade >= 18 and idade <= 25) and (percentual_gordura >= 4 and percentual_gordura <= 6):
    classificacao = 'Excelente'
  elif (sexo == 'M') and (idade >= 18 and idade <= 25) and (percentual_gordura >= 8 and percentual_gordura <= 10):
    classificacao = 'Bom'
  elif (sexo == 'M') and (idade >= 18 and idade <= 25) and (percentual_gordura >= 12 and percentual_gordura <= 13):
    classificacao = 'Acima da média'
  elif (sexo == 'M') and (idade >= 18 and idade <= 25) and (percentual_gordura >= 14 and percentual_gordura <= 16):
    classificacao = 'Média'
  elif (sexo == 'M') and (idade >= 18 and idade <= 25) and (percentual_gordura >= 17 and percentual_gordura <= 20):
    classificacao = 'Abaixo da média'
  elif (sexo == 'M') and (idade >= 18 and idade <= 25) and (percentual_gordura >= 20 and percentual_gordura <= 24):
    classificacao = 'Ruim'
  elif (sexo == 'M') and (idade >= 18 and idade <= 25) and (percentual_gordura >= 26 and percentual_gordura <= 36):
    classificacao = 'Muito ruim'

  ## HOMENS COM IDADE ENTRE 26 ANOS E 35 ANOS DE IDADE 
  elif (sexo == 'M') and (idade >= 26 and idade <= 35) and (percentual_gordura >= 8 and percentual_gordura <= 11):
    classificacao = 'Excelente'
  elif (sexo == 'M') and (idade >= 26 and idade <= 35) and (percentual_gordura >= 12 and percentual_gordura <= 15):
    classificacao = 'Bom'
  elif (sexo == 'M') and (idade >= 26 and idade <= 35) and (percentual_gordura >= 16 and percentual_gordura < 18):
    classificacao = 'Acima da média'
  elif (sexo == 'M') and (idade >= 26 and idade <= 35) and (percentual_gordura >= 18 and percentual_gordura < 20):
    classificacao = 'Média'
  elif (sexo == 'M') and (idade >= 26 and idade <= 35) and (percentual_gordura >= 20 and percentual_gordura < 22):
    classificacao = 'Abaixo da média'
  elif (sexo == 'M') and (idade >= 26 and idade <= 35) and (percentual_gordura >= 22 and percentual_gordura <= 24):
    classificacao = 'Ruim'
  elif (sexo == 'M') and (idade >= 26 and idade <= 35) and (percentual_gordura >= 28 and percentual_gordura <= 36):
    classificacao = 'Muito ruim'

    ## HOMENS COM IDADE ENTRE 36 ANOS E 45 ANOS DE IDADE 
  elif (sexo == 'M') and (idade >= 36 and idade <= 45) and (percentual_gordura >= 10 and percentual_gordura <= 14):
    classificacao = 'Excelente'
  elif (sexo == 'M') and (idade >= 36 and idade <= 45) and (percentual_gordura >= 16 and percentual_gordura <= 18):
    classificacao = 'Bom'
  elif (sexo == 'M') and (idade >= 36 and idade <= 45) and (percentual_gordura >= 19 and percentual_gordura <= 21):
    classificacao = 'Acima da média'
  elif (sexo == 'M') and (idade >= 36 and idade <= 45) and (percentual_gordura >= 21 and percentual_gordura <= 23):
    classificacao = 'Média'
  elif (sexo == 'M') and (idade >= 36 and idade <= 45) and (percentual_gordura >= 24 and percentual_gordura <= 24):
    classificacao = 'Abaixo da média'
  elif (sexo == 'M') and (idade >= 36 and idade <= 45) and (percentual_gordura >= 27 and percentual_gordura <= 29):
    classificacao = 'Ruim'
  elif (sexo == 'M') and (idade >= 36 and idade <= 45) and (percentual_gordura >= 30 and percentual_gordura <= 39):
    classificacao = 'Muito ruim'

  ## HOMENS COM IDADE ENTRE 46 ANOS E 55 ANOS DE IDADE 
  elif (sexo == 'M') and (idade >= 46 and idade <= 55) and (percentual_gordura >= 12 and percentual_gordura <= 16):
    classificacao = 'Excelente'
  elif (sexo == 'M') and (idade >= 46 and idade <= 55) and (percentual_gordura >= 18 and percentual_gordura <= 20):
    classificacao = 'Bom'
  elif (sexo == 'M') and (idade >= 46 and idade <= 55) and (percentual_gordura >= 21 and percentual_gordura <= 23):
    classificacao = 'Acima da média'
  elif (sexo == 'M') and (idade >= 46 and idade <= 55) and (percentual_gordura >= 24 and percentual_gordura <= 25):
    classificacao = 'Média'
  elif (sexo == 'M') and (idade >= 46 and idade <= 55) and (percentual_gordura >= 26 and percentual_gordura <= 27):
    classificacao = 'Abaixo da média'
  elif (sexo == 'M') and (idade >= 46 and idade <= 55) and (percentual_gordura >= 28 and percentual_gordura <= 30):
    classificacao = 'Ruim'
  elif (sexo == 'M') and (idade >= 46 and idade <= 55) and (percentual_gordura >= 32 and percentual_gordura <= 38):
    classificacao = 'Muito ruim'

  ## HOMENS COM IDADE ENTRE 56 ANOS E 65 ANOS DE IDADE 
  elif (sexo == 'M') and (idade >= 56 and idade <= 65) and (percentual_gordura >= 13 and percentual_gordura <= 18):
    classificacao = 'Excelente'
  elif (sexo == 'M') and (idade >= 56 and idade <= 65) and (percentual_gordura >= 20 and percentual_gordura <= 21):
    classificacao = 'Bom'
  elif (sexo == 'M') and (idade >= 56 and idade <= 65) and (percentual_gordura >= 22 and percentual_gordura <= 23):
    classificacao = 'Acima da média'
  elif (sexo == 'M') and (idade >= 56 and idade <= 65) and (percentual_gordura >= 24 and percentual_gordura <= 25):
    classificacao = 'Média'
  elif (sexo == 'M') and (idade >= 56 and idade <= 65) and (percentual_gordura >= 26 and percentual_gordura <= 27):
    classificacao = 'Abaixo da média'
  elif (sexo == 'M') and (idade >= 56 and idade <= 65) and (percentual_gordura >= 28 and percentual_gordura <= 30):
    classificacao = 'Ruim'
  elif (sexo == 'M') and (idade >= 56 and idade <= 65) and (percentual_gordura >= 32 and percentual_gordura <= 38):
    classificacao = 'Muito ruim'

  ########################################################################################################################

  ## MULHERES COM IDADE ENTRE 18 ANOS E 25 ANOS DE IDADE 
  elif (sexo == 'F') and (idade >= 18 and idade <= 25) and (percentual_gordura >= 13 and percentual_gordura <= 16):
    classificacao = 'Excelente'
  elif (sexo == 'F') and (idade >= 18 and idade <= 25) and (percentual_gordura >= 17 and percentual_gordura <= 19):
    classificacao = 'Bom'
  elif (sexo == 'F') and (idade >= 18 and idade <= 25) and (percentual_gordura >= 20 and percentual_gordura <= 22):
    classificacao = 'Acima da média'
  elif (sexo == 'F') and (idade >= 18 and idade <= 25) and (percentual_gordura >= 23 and percentual_gordura <= 25):
    classificacao = 'Média'
  elif (sexo == 'F') and (idade >= 18 and idade <= 25) and (percentual_gordura >= 26 and percentual_gordura <= 28):
    classificacao = 'Abaixo da média'
  elif (sexo == 'F') and (idade >= 18 and idade <= 25) and (percentual_gordura >= 29 and percentual_gordura <= 31):
    classificacao = 'Ruim'
  elif (sexo == 'F') and (idade >= 18 and idade <= 25) and (percentual_gordura >= 33 and percentual_gordura <= 43):
    classificacao = 'Muito ruim'

  ## MULHERES COM IDADE ENTRE 26 ANOS E 35 ANOS DE IDADE 
  elif (sexo == 'F') and (idade >= 26 and idade <= 35) and (percentual_gordura >= 14 and percentual_gordura <= 16):
    classificacao = 'Excelente'
  elif (sexo == 'F') and (idade >= 26 and idade <= 35) and (percentual_gordura >= 18 and percentual_gordura <= 20):
    classificacao = 'Bom'
  elif (sexo == 'F') and (idade >= 26 and idade <= 35) and (percentual_gordura >= 21 and percentual_gordura <= 23):
    classificacao = 'Acima da média'
  elif (sexo == 'F') and (idade >= 26 and idade <= 35) and (percentual_gordura >= 24 and percentual_gordura <= 25):
    classificacao = 'Média'
  elif (sexo == 'F') and (idade >= 26 and idade <= 35) and (percentual_gordura >= 27 and percentual_gordura <= 29):
    classificacao = 'Abaixo da média'
  elif (sexo == 'F') and (idade >= 26 and idade <= 35) and (percentual_gordura >= 31 and percentual_gordura <= 33):
    classificacao = 'Ruim'
  elif (sexo == 'F') and (idade >= 26 and idade <= 35) and (percentual_gordura >= 36 and percentual_gordura <= 49):
    classificacao = 'Muito ruim'

    ## MULHERES COM IDADE ENTRE 36 ANOS E 45 ANOS DE IDADE 
  elif (sexo == 'F') and (idade >= 36 and idade <= 45) and (percentual_gordura >= 16 and percentual_gordura <= 19):
    classificacao = 'Excelente'
  elif (sexo == 'F') and (idade >= 36 and idade <= 45) and (percentual_gordura >= 20 and percentual_gordura <= 23):
    classificacao = 'Bom'
  elif (sexo == 'F') and (idade >= 36 and idade <= 45) and (percentual_gordura >= 24 and percentual_gordura <= 26):
    classificacao = 'Acima da média'
  elif (sexo == 'F') and (idade >= 36 and idade <= 45) and (percentual_gordura >= 27 and percentual_gordura <= 29):
    classificacao = 'Média'
  elif (sexo == 'F') and (idade >= 36 and idade <= 45) and (percentual_gordura >= 30 and percentual_gordura <= 32):
    classificacao = 'Abaixo da média'
  elif (sexo == 'F') and (idade >= 36 and idade <= 45) and (percentual_gordura >= 33 and percentual_gordura <= 36):
    classificacao = 'Ruim'
  elif (sexo == 'F') and (idade >= 36 and idade <= 45) and (percentual_gordura >= 38 and percentual_gordura <= 48):
    classificacao = 'Muito ruim'

  ## MULHERES COM IDADE ENTRE 46 ANOS E 55 ANOS DE IDADE 
  elif (sexo == 'F') and (idade >= 46 and idade <= 55) and (percentual_gordura >= 17 and percentual_gordura <= 21):
    classificacao = 'Excelente'
  elif (sexo == 'F') and (idade >= 46 and idade <= 55) and (percentual_gordura >= 23 and percentual_gordura <= 25):
    classificacao = 'Bom'
  elif (sexo == 'F') and (idade >= 46 and idade <= 55) and (percentual_gordura >= 26 and percentual_gordura <= 28):
    classificacao = 'Acima da média'
  elif (sexo == 'F') and (idade >= 46 and idade <= 55) and (percentual_gordura >= 29 and percentual_gordura <= 31):
    classificacao = 'Média'
  elif (sexo == 'F') and (idade >= 46 and idade <= 55) and (percentual_gordura >= 32 and percentual_gordura <= 34):
    classificacao = 'Abaixo da média'
  elif (sexo == 'F') and (idade >= 46 and idade <= 55) and (percentual_gordura >= 35 and percentual_gordura <= 38):
    classificacao = 'Ruim'
  elif (sexo == 'F') and (idade >= 46 and idade <= 55) and (percentual_gordura >= 39 and percentual_gordura <= 50):
    classificacao = 'Muito ruim'

  ## MULHERES COM IDADE ENTRE 56 ANOS E 65 ANOS DE IDADE 
  elif (sexo == 'F') and (idade >= 56 and idade <= 65) and (percentual_gordura >=   18 and percentual_gordura <= 22):
    classificacao = 'Excelente'
  elif (sexo == 'F') and (idade >= 56 and idade <= 65) and (percentual_gordura >= 24 and percentual_gordura <= 26):
    classificacao = 'Bom'
  elif (sexo == 'F') and (idade >= 56 and idade <= 65) and (percentual_gordura >= 27 and percentual_gordura <= 29):
    classificacao = 'Acima da média'
  elif (sexo == 'F') and (idade >= 56 and idade <= 65) and (percentual_gordura >= 30 and percentual_gordura <= 32):
    classificacao = 'Média'
  elif (sexo == 'F') and (idade >= 56 and idade <= 65) and (percentual_gordura >= 33 and percentual_gordura <= 35):
    classificacao = 'Abaixo da média'
  elif (sexo == 'F') and (idade >= 56 and idade <= 65) and (percentual_gordura >= 36 and percentual_gordura <= 38):
    classificacao = 'Ruim'
  elif (sexo == 'F') and (idade >= 56 and idade <= 65) and (percentual_gordura >= 39 and percentual_gordura <= 49):
    classificacao = 'Muito ruim'

  ## CRIANÇAS E ADOLESCENTES DO SEXO MASCULINO COM IDADE ENTRE 7 ANOS E 17 ANOS
  elif (sexo == 'M') and (idade >= 7 and idade <= 17) and (percentual_gordura <= 6):
    classificacao = 'Excessivamente baixa'
  elif (sexo == 'M') and (idade >= 7 and idade <= 17) and (percentual_gordura > 6 and percentual_gordura <= 10):
    classificacao = 'Baixa'
  elif (sexo == 'M') and (idade >= 7 and idade <= 17) and (percentual_gordura > 10 and percentual_gordura <= 20):
    classificacao = 'Adequada'
  elif (sexo == 'M') and (idade >= 7 and idade <= 17) and (percentual_gordura > 20 and percentual_gordura <= 25):
    classificacao = 'Moderadamente alta'
  elif (sexo == 'M') and (idade >= 7 and idade <= 17) and (percentual_gordura > 25 and percentual_gordura <= 31):
    classificacao = 'Alta'
  elif (sexo == 'M') and (idade >= 7 and idade <= 17) and (percentual_gordura > 31):
    classificacao = 'Excessivamente alta'

 ## CRIANÇAS E ADOLESCENTES DO SEXO FEMININO COM IDADE ENTRE 7 ANOS E 17 ANOS
  elif (sexo == 'F') and (idade >= 7 and idade <= 17) and (percentual_gordura <= 12):
    classificacao = 'Excessivamente baixa'
  elif (sexo == 'F') and (idade >= 7 and idade <= 17) and (percentual_gordura > 12 and percentual_gordura <= 15):
    classificacao = 'Baixa'
  elif (sexo == 'F') and (idade >= 7 and idade <= 17) and (percentual_gordura > 15 and percentual_gordura <= 25):
    classificacao = 'Adequada'
  elif (sexo == 'F') and (idade >= 7 and idade <= 17) and (percentual_gordura > 25 and percentual_gordura <= 30):
    classificacao = 'Moderadamente alta'
  elif (sexo == 'F') and (idade >= 7 and idade <= 17) and (percentual_gordura > 30 and percentual_gordura <= 36):
    classificacao = 'Alta'
  elif (sexo == 'F') and (idade >= 7 and idade <= 17) and (percentual_gordura > 36):
    classificacao = 'Excessivamente alta'
  else:
    classificacao = "Valor fora do intervalo de referência"
    
  return classificacao


class TestStringMethods(unittest.TestCase):
    def teste_01(self):
        self.assertEqual(classifica_percentul_gordura('M', 18, 6), 'Excelente')

    def teste_02(self):
        self.assertEqual(classifica_percentul_gordura('M', 27, 13), 'Bom')

    def teste_03(self):
        self.assertEqual(classifica_percentul_gordura('M', 40, 21), 'Acima da média')

    def teste_04(self):
        self.assertEqual(classifica_percentul_gordura('M', 50, 25), 'Média')

    def teste_05(self):
        self.assertEqual(classifica_percentul_gordura('M', 57, 26), 'Abaixo da média')

    def teste_06(self):
        self.assertEqual(classifica_percentul_gordura('M', 60, 29), 'Ruim')

    def teste_07(self):
        self.assertEqual(classifica_percentul_gordura('M', 19, 27), 'Muito ruim')

    def teste_08(self):
        self.assertEqual(classifica_percentul_gordura('M', 18, 7), 'Valor fora do intervalo de referência')

    def teste_09(self):
        self.assertEqual(classifica_percentul_gordura('F', 18, 13), 'Excelente')

    def teste_10(self):
        self.assertEqual(classifica_percentul_gordura('F', 18, 17), 'Bom')

    def teste_11(self):
        self.assertEqual(classifica_percentul_gordura('F', 18, 20), 'Acima da média')

    def teste_12(self):
        self.assertEqual(classifica_percentul_gordura('F', 18, 23), 'Média')

    def teste_13(self):
        self.assertEqual(classifica_percentul_gordura('F', 18, 26), 'Abaixo da média')

    def teste_14(self):
        self.assertEqual(classifica_percentul_gordura('F', 18, 29), 'Ruim')

    def teste_15(self):
        self.assertEqual(classifica_percentul_gordura('F', 18, 33), 'Muito ruim')

    def teste_16(self):
        self.assertEqual(classifica_percentul_gordura('F', 18, 100), 'Valor fora do intervalo de referência')

    def teste_17(self):
        self.assertEqual(classifica_percentul_gordura('M', 7, 5), 'Excessivamente baixa')

    def teste_18(self):
        self.assertEqual(classifica_percentul_gordura('M', 8, 7), 'Baixa')

    def teste_19(self):
        self.assertEqual(classifica_percentul_gordura('M', 9, 11), 'Adequada')

    def teste_20(self):
        self.assertEqual(classifica_percentul_gordura('M', 10, 21), 'Moderadamente alta')

    def teste_21(self):
        self.assertEqual(classifica_percentul_gordura('M', 11, 26), 'Alta')

    def teste_22(self):
        self.assertEqual(classifica_percentul_gordura('M', 12, 100), 'Excessivamente alta')

    def teste_23(self):
        self.assertEqual(classifica_percentul_gordura('F', 7, 10), 'Excessivamente baixa')

    def teste_24(self):
        self.assertEqual(classifica_percentul_gordura('F', 8, 13), 'Baixa')

    def teste_25(self):
        self.assertEqual(classifica_percentul_gordura('F', 9, 16), 'Adequada')

    def teste_26(self):
        self.assertEqual(classifica_percentul_gordura('F', 10, 26), 'Moderadamente alta')

    def teste_27(self):
        self.assertEqual(classifica_percentul_gordura('F', 11, 31), 'Alta')

    def teste_28(self):
        self.assertEqual(classifica_percentul_gordura('F', 12, 37), 'Excessivamente alta')

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

print('')
print('TESTES AUTOMATIADOS PARA VALIDAÇÃO DA FUNÇÃO CLASSIFICA_PERCENTUAL_GORDURA()')
print('')
print(runTests())

  


