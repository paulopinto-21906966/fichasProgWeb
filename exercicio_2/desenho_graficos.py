# O modulo matplotlib permite fazer desenho de gráficos
from matplotlib import pyplot as plt


def faz_grafico_queijos(titulo, lista_chaves, lista_valores):
    plt.pie(lista_valores, labels=lista_chaves, autopct='%1.0f%%')
    plt.title(titulo)
    plt.show()


def faz_grafico_barras(titulo, lista_chaves, lista_valores):
    plt.bar(lista_chaves, lista_valores)
    plt.title(titulo)
    plt.show()


lista_chaves = ['HTML & CSS', 'Python & Django', 'JavaScript & React']
lista_valores = [5, 5, 3]
titulo = 'Programação Web'
faz_grafico_queijos(titulo, lista_chaves, lista_valores)
faz_grafico_barras(titulo, lista_chaves, lista_valores)
