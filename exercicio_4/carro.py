import random


class automovel:
    def __init__(self, c=0, q=0, con=0):
        self.id = ''.join([str(random.randint(0, 9)) for rand in range(0, 5)])
        self.cap_dep = c
        self.quant_comb = q
        self.consumo = con

    def mostra(self):
        print(f'O carro tem{self.cap_dep} Litros')

    def combustivel(self):
        return self.quant_comb

    def autonomia(self):
        return self.quant_comb / (self.consumo / 100)

    def abastece(self, n_litros):
        if self.quant_comb + n_litros > self.cap_dep:
            print("Tentou abastecer demasiado!")
            return -1
        else:
            self.quant_comb += n_litros
            print(f"Abasteceu {n_litros} L, total: {self.quant_comb} L")
            print(self.autonomia())
            return 1

    def percorre(self, n_kms):
        consumoPrevisto = self.consumo / 100 * n_kms
        if consumoPrevisto > self.quant_comb:
            print("Não tem combustível suficiente!")
            return -1
        else:
            self.quant_comb -= consumoPrevisto
            print(f"Percorreu {n_kms} km e gastou {consumoPrevisto} L")
            print(self.autonomia())
            return 1

    def __repr__(self):
        return f"""
Carro {self.id} tem:
    capacidade : {self.cap_dep}
    gas in the tank: {self.quant_comb}
    consumo : {self.consumo}
"""

    def __str__(self):
        return f"""
Carro {self.id} tem:
    capacidade : {self.cap_dep}
    quantidade : {self.quant_comb}
    consumo : {self.consumo}
"""


##TODO: MENU

def menu():
    pass


def main():
    # carro = automovel(60, 40, 8)
    # print(carro)
    # print(carro.autonomia())
    # carro.percorre(10)
    # carro.percorre(1000)
    # carro.abastece(10)
    # carro.abastece(100)
    # print(carro)

    a1 = automovel(60, 10, 15)
    print(a1.autonomia())

    a1.abastece(45)
    a1.percorre(150)
    a1.percorre(250)

    pass


if __name__ == "__main__":
    main()
