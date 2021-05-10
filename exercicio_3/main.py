from exercicio_3 import analise_tree as at


def main():
    pasta = at.pede_pasta()

    soma = at.calcula_tamanho_pasta(pasta, 0)
    print("{:1.2f}mB em {}".format(soma, pasta))


if __name__ == '__main__':
    main()
