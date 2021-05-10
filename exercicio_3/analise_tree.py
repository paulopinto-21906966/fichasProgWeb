import os


def pede_pasta():
    while not os.path.isdir(folder := input("Insira um caminho para a pasta: ")):
        print("experimente " + os.getcwd())

    return folder


def calcula_tamanho_pasta(pasta, level):
    soma = 0

    for file in os.listdir(pasta):
        filedir = (os.path.join(pasta, file))
        print('|\t' * level + file)
        # print(fileDir)

        if os.path.isfile(filedir):
            soma += os.path.getsize(filedir) / 2 ** 20

        if os.path.isdir(filedir):
            soma += calcula_tamanho_pasta(filedir, 1 + level)

    return soma
