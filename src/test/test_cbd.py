import os
import sys

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
sys.path.insert(0, PROJECT_DIR)

from app.cbd import Cbd

class TestClass:

    def teste_rendimento_bruto(self):
        cbd = Cbd(1400,8.5,60)
        assert (cbd.vi * (1 + (cbd.i/100))**(cbd.n/365)) - cbd.vi == cbd.rendimento_bruto()
