class Carro:
    velMax = 0
    ligado = False
    cor = ""

    def __init__(self, v, l, c):
        self.velMax = v
        self.ligado = l
        self.cor = c

    def show(self):
        print(f"Velocidade máxima: {self.velMax}")
        print(f"Cor: {self.cor}")
        estado = "Sim" if self.ligado else "Não"
        print(f"Ligado: {estado}")

    def ligar(self):
        self.ligado = True


c1 = Carro(200, False, "Preto")

c1.show()

c1.ligar()

c1.show()

