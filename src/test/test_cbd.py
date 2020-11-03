import os
import sys

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
sys.path.insert(0, PROJECT_DIR)

from app.cbd import Cbd

class TestClass:

    def teste_rendimento_bruto(self):
        cbd = Cbd(1400,8.5,60)
        assert (18.90102 == round(cbd.rendimento_bruto(), 5)) # utilizando round para testar com 5 casas decimais

    def teste_rendimento_bruto_2(self):
        cbd = Cbd(1200, 8.5, 60)
        assert (16.20088 == round(cbd.rendimento_bruto(), 5)) # utilizando round para testar com 5 casas decimais

    def teste_imposto_de_renda(self):
        cbd = Cbd(1400,8.5,60)
        assert (500 == cbd.imposto_de_renda())

    def teste_rendimento_liquido(self):
        cbd = Cbd(1400,8.5,60)
        assert (500 == cbd.rendimento_liquido())

    def teste_rendimento_liquido_2(self):
        cbd = Cbd(1000,8.5,60)
        assert (1.3500731656813798 == cbd.rendimento_liquido())