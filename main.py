import random

# definindo tamanho da matriz
tamanho_matriz = int(input("Defina o tamanho da matriz quadrada: "))
tamanho_linhas_matriz = tamanho_matriz
tamanho_colunas_matriz = tamanho_matriz

# criando lista de palavras
palavras = []
print("Você deve digitar até", tamanho_matriz,"palavras com no máximo", tamanho_matriz,"letras")
for indice_palavra in range(0, tamanho_matriz):
    sair = 0
    digite_palavra = 1
    while(digite_palavra == 1):
        palavra_digitada = str(input(f'Digite a {indice_palavra+1}a palavra: '))
        palavra_digitada = palavra_digitada.replace(" ", "")
        if not palavra_digitada or palavra_digitada.replace(" ", "") == "":
            sair = 1
            break
        else:
            if(len(palavra_digitada) <= tamanho_matriz):
                palavras.append(palavra_digitada)
                digite_palavra = 0
            else:
                print("A palavra possui um tamanho não permitido!")
                digite_palavra = 1
    if(sair == 1):
        break

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
for palavra in palavras:
    tamanho_palavra = len(palavra)
    direcao = random.choice(["horizontal", "vertical", "diagonal_para_direita", "diagonal_para_esquerda"])
    if(direcao == "horizontal"):
        linha_palavra = random.randint(0, tamanho_colunas_matriz-1)
        coluna_palavra = random.randint(0, tamanho_linhas_matriz-tamanho_palavra)
        for letra in palavra:
            matriz[linha_palavra][coluna_palavra] = letra
            coluna_palavra += 1
    elif(direcao == "vertical"):
        linha_palavra = random.randint(0, tamanho_colunas_matriz-tamanho_palavra)
        coluna_palavra = random.randint(0, tamanho_linhas_matriz-1)
        for letra in palavra:
            matriz[linha_palavra][coluna_palavra] = letra
            linha_palavra += 1
    elif(direcao == "diagonal_para_direita"):
        linha_palavra = random.randint(0, tamanho_colunas_matriz-tamanho_palavra)
        coluna_palavra = random.randint(0, tamanho_linhas_matriz-tamanho_palavra)
        for letra in palavra:
            matriz[linha_palavra][coluna_palavra] = letra
            linha_palavra += 1
            coluna_palavra += 1
    elif(direcao == "diagonal_para_esquerda"):
        linha_palavra = random.randint(0, tamanho_colunas_matriz-tamanho_palavra)
        coluna_palavra = random.randint(tamanho_palavra-1, tamanho_linhas_matriz-1)
        for letra in palavra:
            matriz[linha_palavra][coluna_palavra] = letra
            linha_palavra += 1
            coluna_palavra -= 1

# printando a matriz
for linha in matriz:
    print(linha)