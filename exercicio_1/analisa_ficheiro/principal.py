from exercicio_1.analisa_ficheiro import acessorio as ace
from exercicio_1.analisa_ficheiro import calculos as calc
import json


def main():
    ace.pede_nome()
    print(ace.gera_nome("historia.txt"))

    print(calc.calcula_linhas("text.txt"))
    print(calc.calcula_caracteres("text.txt"))
    print(calc.calcula_palavra_comprida("text.txt"))
    counter = (calc.calcula_ocorrencia_de_letras("text.txt"))
    print(counter)

    with open('resultados.json', 'w') as json_file:
        json.dump(counter, json_file)


if __name__ == "__main__":
    main()
