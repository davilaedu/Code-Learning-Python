class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2

    def muda_canal_para_baixo(self):
        self.canal -= 1

    def muda_canal_para_cima(self):
        self.canal += 1


tv = Televisao()
print tv.muda_canal_para_cima()
print tv.muda_canal_para_cima()
print tv.canal
