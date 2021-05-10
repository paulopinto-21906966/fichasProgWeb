import os, csv
from collections import defaultdict
from collections import Counter
from matplotlib import pyplot as plt
import pandas as pd


def pede_pasta():
    while not os.path.isdir(input("Insira um caminho para a pasta: ")):
        print("experimente " + os.getcwd())

    return True


def faz_calculos():
    # filesTuples = list([file.split(".") for file in os.listdir() if "." in file])
    # print(filesTuples)
    # print({extension: filename for filename, extension in filesTuples})

    extensionCounter = Counter(list([file.split(".")[1] for file in os.listdir() if "." in file]))
    # print(extensionCounter)

    fileDict = defaultdict(int)

    for filename, extension in list([file.split(".") for file in os.listdir() if "." in file]):
        fileDict[extension] += os.path.getsize(filename + "." + extension) / 2 ** 10

    for file in fileDict.keys():
        fileDict[file] = {'volume': "{:0.2f}".format(fileDict[file]), 'quantidade': extensionCounter[file]}

    return fileDict


def guarda_resultados(dirInfo, fname='ficheiros.csv'):
    with open(fname, 'w', newline='') as ficheiro:
        writer = csv.DictWriter(ficheiro, fieldnames=['extension', 'quantidade', 'volume'])
        writer.writeheader()
        for file in dirInfo:
            # print(dirInfo[file])
            writer.writerow(
                {'extension': file, 'quantidade': dirInfo[file]['quantidade'], 'volume': dirInfo[file]['volume']})
    return print("data stored in " + fname)


def faz_grafico_queijos(fname='ficheiros.csv'):
    extensionDf = pd.read_csv(fname)

    extensions = extensionDf['extension']
    columns = extensionDf['volume']

    plt.pie(columns, labels=extensions, autopct='%1.1f%%')
    plt.title('Extensões por tamanho')
    plt.show()


def faz_grafico_barras(fname='ficheiros.csv'):
    extensionDf = pd.read_csv(fname)

    extensions = extensionDf['extension']
    columns = extensionDf['quantidade']

    plt.bar(extensions, columns)
    plt.title('Extensões por quantidade de ficheiros')
    plt.show()
