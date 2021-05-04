from os import path


def pede_nome():
    while not path.exists(input("Digite o nome do ficheiro pretendido (inclua extensão): ")):
        pass
    return "existe"


def gera_nome(fname):
    return fname.split(".")[0] + ".json"
