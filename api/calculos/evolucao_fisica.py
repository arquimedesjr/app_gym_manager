import unittest
import hashlib

class CalculadorEvolucaoFisica():
    def evolucao_fisica(self, medida_01, medida_02):
        if medida_02 > medida_01:
            evolucao_fisica = ((medida_02/medida_01)-1)*100
            evolucao_fisica = round(evolucao_fisica, 2)
            evolucao_fisica = str(evolucao_fisica)
            status = "Suas medidas aumentaram em {}%".format(evolucao_fisica)

        elif medida_02 < medida_01:
            evolucao_fisica = ((medida_02/medida_01)-1)*(-100)
            evolucao_fisica = round(evolucao_fisica, 2)
            evolucao_fisica = str(evolucao_fisica)
            status = "Suas medidas diminuíram em {}%".format(evolucao_fisica)

        else: 
            status = 'Você se manteve com as mesmas medidas'
        print(status)
        return status

class TestStringMethods(unittest.TestCase):
    def teste_01(self):
        self.assertEqual(CalculadorEvolucaoFisica().evolucao_fisica(5.5, 6.6),"Suas medidas aumentaram em 20.0%")

    def teste_02(self):
        self.assertEqual(CalculadorEvolucaoFisica().evolucao_fisica(5, 10),"Suas medidas aumentaram em 100.0%")

    def teste_03(self):
        self.assertEqual(CalculadorEvolucaoFisica().evolucao_fisica(5, 15),"Suas medidas aumentaram em 200.0%")

    def teste_04(self):
        self.assertEqual(CalculadorEvolucaoFisica().evolucao_fisica(5.5, 4.4),"Suas medidas diminuíram em 20.0%")

    def teste_05(self):
        self.assertEqual(CalculadorEvolucaoFisica().evolucao_fisica(5, 1),"Suas medidas diminuíram em 80.0%")

    def teste_06(self):
        self.assertEqual(CalculadorEvolucaoFisica().evolucao_fisica(5, 0),"Suas medidas diminuíram em 100.0%")

    def teste_07(self):
        self.assertEqual(CalculadorEvolucaoFisica().evolucao_fisica(5, 5),"Você se manteve com as mesmas medidas")

    def teste_08(self):
        self.assertEqual(CalculadorEvolucaoFisica().evolucao_fisica(6, 6),"Você se manteve com as mesmas medidas")

    def teste_09(self):
        self.assertEqual(CalculadorEvolucaoFisica().evolucao_fisica(7, 7),"Você se manteve com as mesmas medidas")

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

print('')
print('TESTES AUTOMATIADOS PARA VALIDAÇÃO DA FUNÇÃO EVOLUCAO_FISICA()')
print('')
print(runTests())