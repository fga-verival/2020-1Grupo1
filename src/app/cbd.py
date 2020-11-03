class Cbd:
    def __init__(self, vi: float, i: float, n: int):
        self.vi = vi
        self.i = i
        self.n = n

    def rendimento_bruto(self):
        return 500 #falsificação

    def imposto_de_renda(self):
        return 500 #falsificação

    def rendimento_liquido(self):
        # rl = rendimento liquido
        rl = (((self.vi + self.rendimento_bruto())/self.vi) * 100 ) - 100
        return rl