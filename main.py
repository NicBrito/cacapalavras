import random

# definindo tamanho da matriz
tamanho_matriz = int(input("Defina o tamanho da matriz quadrada: "))
tamanho_linhas_matriz = tamanho_matriz
tamanho_colunas_matriz = tamanho_matriz

# criando lista de palavras
palavras = []
print("Você deve digitar até ", tamanho_matriz, " palavras de tamanho ", tamanho_matriz)
for x in range(0, tamanho_matriz):
    digite_palavra = 1
    while(digite_palavra == 1):
        palavra_digitada = str(input(f'Digite a {x+1}a palavra: '))
        if(len(palavra_digitada) <= tamanho_matriz):
            palavras.append(palavra_digitada)
            digite_palavra = 0
        else:
            print("A palavra possui um tamanho não permitido!")
            digite_palavra = 1

# lista com as letras do alfabeto
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
          'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
          'u', 'v', 'w', 'x', 'y', 'z']

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