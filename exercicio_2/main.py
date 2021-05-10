from exercicio_2 import analise_pasta as ap


# from exercicio_2 import desenho_graficos
# from exercicio_2 import escreve_csv


def main():
    ap.pede_pasta()
    dirInfo = ap.faz_calculos()
    # print(dirInfo)
    ap.guarda_resultados(dirInfo)
    ap.faz_grafico_queijos()
    ap.faz_grafico_barras()


if __name__ == '__main__':
    main()
