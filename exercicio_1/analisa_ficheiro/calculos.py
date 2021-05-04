import collections as c


def calcula_linhas(fname):
    # with open(fname, "r") as fp:
    #     dados = fp.readlines()

    return f'O ficheiro tem {len(open(fname, "r").readlines())} linhas'


def calcula_caracteres(fname):
    # with open(fname, "r") as fp:
    #     dados = fp.read()
    #
    # return f'O ficheiro tem {len(dados)} caracteres'
    return f'O ficheiro tem {len(open(fname, "r").read())} caracteres'


def calcula_palavra_comprida(fname):
    # with open(fname, "r") as fp:
    #     dados = fp.read().split()
    #
    # return max(dados, key=len)
    return f'Palavra mais comprida: {max(open(fname, "r").read().split(), key=len)}'


def calcula_ocorrencia_de_letras(fname):
    # with open(fname, "r") as fp:
    #     dados = fp.read()
    #
    # return c.Counter(dados)
    return c.Counter(open(fname, "r").read())
