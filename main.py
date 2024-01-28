import random

# lista com as palavras que devem ser encontradas
palavras = ["amor", "paz", "raiva", "python", "lar"]

# lista com as letras do alfabeto
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
          'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
          'u', 'v', 'w', 'x', 'y', 'z']

# definindo tamanho da matriz
tamanho_linhas_matriz = 6
tamanho_colunas_matriz = 6

# criando a matriz com letras aleatorias
matriz = []
for numero_linha in range(0, tamanho_colunas_matriz):
    linha = []
    for numero_coluna in range(0, tamanho_linhas_matriz):
        letra_aleatoria = random.choice(letras)
        linha.append(letra_aleatoria)
    matriz.append(linha)

# colocando as palavras na matriz
linha_matriz = 0
for palavra in palavras:
    coluna_matriz = 0
    for letra in palavra:
        matriz[linha_matriz][coluna_matriz] = letra
        coluna_matriz += 1
    linha_matriz += 1

# printando a matriz
for x in matriz:
    print(x)