# coding: utf-8


def cria_matriz(tamanho):
    matriz = []
    for linha in range(8):
        lcoluna = []
        for coluna in range(8):
            lcoluna.append([])
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


matriz = cria_matriz(8)
for l in matriz:
    #print(l)
    for c in l:
        #print(c)
        c.append(1)

mostra_matriz(matriz)
