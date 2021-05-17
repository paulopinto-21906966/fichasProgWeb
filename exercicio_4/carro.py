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


def geraCarro(aleatorio=0):
    if aleatorio == 1:
        return automovel(random.randint(40, 70), random.randint(0, 40), random.randint(5, 15))

    capacidade, quantidade, consumo = 0, 0, 0
    while capacidade := input("Digite a sua capacidade") and capacidade not in range(0, 200):
        print("digite um numero inteiro para a capacidade")

    while quantidade := input("Digite a sua quantidade") and quantidade not in range(0, 200):
        print("digite um numero inteiro para a quantidade")

    while consumo := input("Digite a sua consumo") and consumo not in range(0, 200):
        print("digite um numero inteiro para a consumo")

    return automovel(capacidade, quantidade, consumo)


def menuEscolha():
    while 1:
        escolha = input("""
    Escolha a opção:
         1. Gerar Carro
         2. Gerar Carro aleatório
         3. Sair
""")
        escolha = int(escolha)
        if int(escolha) in range(0, 4):
            break

    if escolha == 1:
        return geraCarro()
    if escolha == 2:
        return geraCarro(1)
    if escolha == 3:
        rip = 1 / 0


def menuCarro(carro):
    while 1:
        escolha = input("""
    Escolha a opção:
         1. Mostrar Carro
         2. Andar
         3. Abastecer
         4. Ver Combustível
         5. Ver Autonomia
         6. Sair
""")
        escolha = int(escolha)
        if escolha not in range(0, 6):
            continue

        # TODO: passar para funções, its a jumbled messsss
        if escolha == 1:
            print(carro)
        if escolha == 2:
            carro.percorre(int(input("Digite quanto quer percorrer: ")))
        if escolha == 3:
            carro.abastece(int(input("Digite quanto quer abastecer: ")))
        if escolha == 4:
            print(carro.combustivel())
        if escolha == 5:
            print(carro.autonomia())
        if escolha == 6:
            rip = 1 / 0
    return


def menu():
    carro = menuEscolha()

    print(carro)

    menuCarro(carro)


def main():
    # a1 = automovel(60, 10, 15)
    # print(a1.autonomia())
    #
    # a1.abastece(45)
    # a1.percorre(150)
    # a1.percorre(250)
    menu()


if __name__ == "__main__":
    main()
