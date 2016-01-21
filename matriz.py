# coding: utf-8


def cria_matriz(tamanho):
    matriz = []
    for linha in range(8):
        lcoluna = []
        for coluna in range(8):
            lcoluna.append(0)
        matriz.append(lcoluna)
    return matriz


def mostra_matriz(matriz):
    for linha in matriz:
        rlinha = ""
        for coluna in linha:
            if coluna:
                rlinha += "1 "
            else:
                rlinha += "0 "
        print(rlinha)


def preenche_com_1(matriz):
    for l in range(len(matriz)):
        for c in range(len(matriz[0])):
            matriz[l][c] = 1


matriz = cria_matriz(8)

mostra_matriz(matriz)
