import os
import sys

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
sys.path.insert(0, PROJECT_DIR)

from app.cbd import Cbd

class TestClass:

    def teste_rendimento_bruto(self):
        cbd = Cbd(1400,8.5,60)
        assert (500 == cbd.rendimento_bruto())

    def teste_rendimento_bruto_2(self):
        cbd = Cbd(1400, 8.5, 60)
        assert (600 == cbd.rendimento_bruto())
