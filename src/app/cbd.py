class Cbd:
    def __init__(self, vi: float, i: float, n: int):
        self.vi = vi
        self.i = i
        self.n = n

    def rendimento_bruto(self):
        valor_rendido = self.vi * (1 + (self.i/100))**(self.n/365)
        rb = valor_rendido - self.vi
        return rb

    def imposto_de_renda(self):
        if self.n <= 180:
            aliquota_de_imposto = 22.5
        elif self.n > 180 & self.n <= 360:
            aliquota_de_imposto = 20
        elif self.n > 360 & self.n <= 720:
            aliquota_de_imposto = 17.5
        else:
            aliquota_de_imposto = 15

        # ir = imposto de renda
        ir = self.rendimento_bruto() * (aliquota_de_imposto/100)
        return ir

    def rendimento_liquido(self):
        # rl = rendimento liquido
        rl = (((self.vi + self.rendimento_bruto())/self.vi) * 100 ) - 100
        return rl