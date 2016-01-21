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


def linha_diagonal(matriz):
    tamanho = len(matriz)
    for l in range(tamanho):
        for c in range(tamanho):
            if l == c:
                matriz[l][c] = 1


def quadrado(matriz, lado):
    tamanho = len(matriz)
    meio = int(tamanho/2)
    print(meio)
    for l in range(tamanho):
        for c in range(tamanho):
            if (l >= meio - lado and l < meio + lado) \
            and (c >= meio - lado and c < meio + lado):
                matriz[l][c] = 1


def quadrado_vazado(matriz, lado):
    tamanho = len(matriz)
    meio = tamanho/2 - 0.5
    print(meio)
    for l in range(tamanho):
        for c in range(tamanho):
            if lado == int(abs(meio - l)) and lado >= int(abs(meio - c)) \
            or lado == int(abs(meio - c)) and lado >= int(abs(meio - l)): 
                matriz[l][c] = 1


matriz = cria_matriz(8)
quadrado_vazado(matriz, 0)
mostra_matriz(matriz)
