import random

# lista com as letras do alfabeto
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
          'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
          'u', 'v', 'w', 'x', 'y', 'z']

# printando a matriz
def printar_matriz(matriz):
    for linha in matriz: # printando linha por linha da matriz
        print(linha) # printando linha da matriz

# printando as palavras
def printar_palavras(palavras):
    print("Palavras:", palavras) # printando a lista de palavras

# definindo tamanho da matriz
def definir_tamanho_matriz():
    tamanho_matriz = int(input("Defina o tamanho da matriz quadrada: ")) # definindo o tamanho da matriz
    tamanho_linhas_matriz = tamanho_matriz # definindo o tamanho das linhas da matriz
    tamanho_colunas_matriz = tamanho_matriz # definindo o tamanho das colunas da matriz
    return tamanho_matriz, tamanho_linhas_matriz, tamanho_colunas_matriz # retornando valores da matriz

# criando lista de palavras
def criar_palavras(tamanho_matriz):
    palavras = [] # criando lista de palavras vazia
    # informando a quantidade de palavras que o usuário deve digitar
    print("Você deve digitar até", tamanho_matriz, "palavras com no máximo", tamanho_matriz, "letras")
    # percorrendo a quantidade de palavras que o usuário deve digitar
    for indice_palavra in range(0, tamanho_matriz):
        sair = 0 # permitir digitar menos palavras que o máximo possível
        digite_palavra = 1 # permitir a digitação de uma palavra
        # caso deva digitar uma nova palavra
        while(digite_palavra == 1):
            # pegando a palavra digitada
            palavra_digitada = str(input(f'Digite a {indice_palavra+1}a palavra: '))
            # removendo espaços da palavra digitada
            palavra_digitada = palavra_digitada.replace(" ", "")
            # caso o usuário não digite nada ou apenas espaços
            if not palavra_digitada or palavra_digitada.replace(" ", "") == "":
                sair = 1 # finalizando a digitação de palavras antes do máximo possível
                break # finalizando a digitação de palavras
            # caso o usuário digite uma palavra
            else:
                # caso a palavra possua um tamanho permitido
                if(len(palavra_digitada) <= tamanho_matriz):
                    palavras.append(palavra_digitada) # adicionando palavra na lista de palavras
                    digite_palavra = 0 # permitir a digitação de uma nova palavra
                # caso a palavra possua um tamanho não permitido
                else:
                    # informando que a palavra possui um tamanho não permitido
                    print("A palavra possui um tamanho não permitido!")
                    digite_palavra = 1 # não permitir a digitação de uma nova palavra
                                       # até que o usuário digite uma palavra com tamanho permitido
        # caso deva finalizar a digitação de palavras antes do máximo possível
        if(sair == 1):
            break # finalizando a digitação de palavras
    return palavras # retornando lista de palavras

# criando a matriz do tamanho definido e a preenchendo com vazios
def criar_matriz(tamanho_linhas_matriz, tamanho_colunas_matriz):
    # print("CRIANDO MATRIZ")
    matriz = [] # criando matriz vazia
    for numero_linha in range(0, tamanho_colunas_matriz): # percorrendo linha por linha da matriz
        linha = [] # criando linha vazia
        for numero_coluna in range(0, tamanho_linhas_matriz): # percorrendo coluna por coluna da matriz
            linha.append("") # adicionando um espaço na linha
        matriz.append(linha) # adicionando linha na matriz
    # printar_matriz(matriz) # printando matriz
    return matriz # retornando matriz

# preenchendo a matriz com letras aleatorias no lugar dos vazios
def preenchendo_matriz(matriz, tamanho_linhas_matriz, tamanho_colunas_matriz):
    # print("PREENCHENDO MATRIZ")
    for numero_linha in range(0, tamanho_colunas_matriz): # percorrendo linha por linha da matriz
        for numero_coluna in range(0, tamanho_linhas_matriz): # percorrendo coluna por coluna da matriz
            if(matriz[numero_linha][numero_coluna] == ""): # caso a posição da matriz seja um vazio
                letra_aleatoria = random.choice(letras) # escolhendo letra aleatoria
                matriz[numero_linha][numero_coluna] = letra_aleatoria # adicionando letra aleatoria na linha
    return matriz # retornando matriz

# função para colocar as palavras na matriz
def colocando_palavras_na_matriz(matriz, palavra, direcao, linha_palavra, coluna_palavra):
    # print("COLOCANDO PALAVRA NA MATRIZ")
    if(direcao == "horizontal"): # caso a direção seja horizontal
        for letra in palavra:
            matriz[linha_palavra][coluna_palavra] = letra
            coluna_palavra += 1
    elif(direcao == "vertical"): # caso a direção seja vertical
        for letra in palavra:
            matriz[linha_palavra][coluna_palavra] = letra
            linha_palavra += 1
    elif(direcao == "diagonal_para_direita"): # caso a direção seja diagonal para a direita
        for letra in palavra:
            matriz[linha_palavra][coluna_palavra] = letra
            linha_palavra += 1
            coluna_palavra += 1
    elif(direcao == "diagonal_para_esquerda"): # caso a direção seja diagonal para a esquerda
        for letra in palavra:
            matriz[linha_palavra][coluna_palavra] = letra
            linha_palavra += 1
            coluna_palavra -= 1

# função para checar sobreposição de palavras na matriz
def checar_sobreposicao_palavras(palavra_existente_na_matriz):
    # print("CHECANDO SOBREPOSIÇÃO DE PALAVRAS NA MATRIZ")
    if(palavra_existente_na_matriz == ""): # caso a palavra existente na matriz seja vazia
        # print("Não vai sobrepor outra palavra")
        return False # não vai sobrepor outra palavra
    else: # caso a palavra existente na matriz não seja vazia
        # print("Vai sobrepor outra palavra")
        return True # vai sobrepor outra palavra

# função para pegar a palavra que já existe na matriz
def checar_palavra_existente_na_matriz(matriz, direcao, tamanho_palavra, linha_palavra, coluna_palavra):
    # print("CHECANDO PALAVRA EXISTENTE NA MATRIZ")
    palavra_existente_na_posicao = "" # criando variável para armazenar a palavra que já existe na posição
    if(direcao == "horizontal"): # caso a direção seja horizontal
        for indice in range(0, tamanho_palavra): # percorrendo a quantidade de letras da palavra
            # adicionando a letra existente na matriz
            palavra_existente_na_posicao += matriz[linha_palavra][coluna_palavra]
            coluna_palavra += 1 # selecionado próxima coluna para pegar a próxima letra da palavra
    elif(direcao == "vertical"): # caso a direção seja vertical
        for indice in range(0, tamanho_palavra): # percorrendo a quantidade de letras da palavra
            # adicionando a letra existente na matriz
            palavra_existente_na_posicao += matriz[linha_palavra][coluna_palavra]
            linha_palavra += 1
    elif(direcao == "diagonal_para_direita"): # caso a direção seja diagonal para a direita
        for indice in range(0, tamanho_palavra): # percorrendo a quantidade de letras da palavra
            # adicionando a letra existente na matriz
            palavra_existente_na_posicao += matriz[linha_palavra][coluna_palavra]
            linha_palavra += 1
            coluna_palavra += 1
    elif(direcao == "diagonal_para_esquerda"): # caso a direção seja diagonal para a esquerda
        for indice in range(0, tamanho_palavra): # percorrendo a quantidade de letras da palavra
            # adicionando a letra existente na matriz
            palavra_existente_na_posicao += matriz[linha_palavra][coluna_palavra]
            linha_palavra += 1
            coluna_palavra -= 1
    # print("Palavra existente na posição:", palavra_existente_na_posicao) # printando a palavra que já existe na posição
    return palavra_existente_na_posicao # retornando a palavra que já existe na posição

# função para escolher posição aleatória para a palavra
def escolher_posicao_aleatoria_para_palavra(direcao, tamanho_linhas_matriz, tamanho_colunas_matriz, tamanho_palavra):
    if(direcao == "horizontal"): # caso a direção seja horizontal
        # escolhendo posicao aleatoria para a palavra
        linha_palavra = random.randint(0, tamanho_colunas_matriz-1)
        coluna_palavra = random.randint(0, tamanho_linhas_matriz-tamanho_palavra)
    elif(direcao == "vertical"): # caso a direção seja vertical
        # escolhendo posicao aleatoria para a palavra
        linha_palavra = random.randint(0, tamanho_colunas_matriz-tamanho_palavra)
        coluna_palavra = random.randint(0, tamanho_linhas_matriz-1)
    elif(direcao == "diagonal_para_direita"): # caso a direção seja diagonal para a direita
        # escolhendo posicao aleatoria para a palavra
        linha_palavra = random.randint(0, tamanho_colunas_matriz-tamanho_palavra)
        coluna_palavra = random.randint(0, tamanho_linhas_matriz-tamanho_palavra)
    elif(direcao == "diagonal_para_esquerda"): # caso a direção seja diagonal para a esquerda
        # escolhendo posicao aleatoria para a palavra
        linha_palavra = random.randint(0, tamanho_colunas_matriz-tamanho_palavra)
        coluna_palavra = random.randint(tamanho_palavra-1, tamanho_linhas_matriz-1)
    else: # caso a direção não seja nenhuma das anteriores
        linha_palavra = 0
        coluna_palavra = 0
    return linha_palavra, coluna_palavra # retornando a linha e a coluna da palavra

# função para colocar as palavras na posição escolhida
def colocar_palavras_na_posicao(matriz, palavras, palavra, direcao, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz):
    # permitir a escolha de uma posição para a palavra
    escolher_posicao = True
    # caso deva escolher uma nova posição para a palavra
    while(escolher_posicao == True):
        # escolhendo posicao aleatoria para a palavra
        linha_palavra, coluna_palavra = escolher_posicao_aleatoria_para_palavra(direcao, tamanho_linhas_matriz, tamanho_colunas_matriz, tamanho_palavra)
        # checar palavra que já existe nessa posição na matriz
        palavra_existente_na_matriz = checar_palavra_existente_na_matriz(matriz, direcao, tamanho_palavra, linha_palavra, coluna_palavra)
        # checar se a palavra vai sobrepor outra palavra
        palavra_vai_sobrepor_outra = checar_sobreposicao_palavras(palavra_existente_na_matriz)
        # se a palavra for sobrescrever outra, escolher nova posicao
        if(palavra_vai_sobrepor_outra == True):
            # permitir a escolha de uma nova posição para a palavra
            escolher_posicao = True
        # se a palavra não for sobrescrever outra, colocar na matriz
        else:
            # não permitir a escolha de uma nova posição para a palavra
            escolher_posicao = False
            # colocando a palavra na matriz
            colocando_palavras_na_matriz(matriz, palavra, direcao, linha_palavra, coluna_palavra)

# colocando as palavras na matriz
def colocar_palavras_na_matriz(matriz, palavras, tamanho_linhas_matriz, tamanho_colunas_matriz):
    for palavra in palavras: # para cada palavra na lista de palavras
        tamanho_palavra = len(palavra) # tamanho da palavra
        # escolhendo posicao aleatoria para a palavra
        direcao = random.choice(["horizontal", "vertical", "diagonal_para_direita", "diagonal_para_esquerda"])
        # direcao = "horizontal" # forçando a direcao horizontal
        # chamar a função para colocar as palavras na posição escolhida
        colocar_palavras_na_posicao(matriz, palavras, palavra, direcao, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz)
        # printar_matriz(matriz) # printando matriz

# função principal
def main():
    # definindo o tamanho da matriz
    tamanho_matriz, tamanho_linhas_matriz, tamanho_colunas_matriz = definir_tamanho_matriz()
    # criando a matriz do tamanho definido e a preenchendo com vazios
    matriz = criar_matriz(tamanho_linhas_matriz, tamanho_colunas_matriz)
    # criando as palavras
    palavras = criar_palavras(tamanho_matriz)
    # colocando as palavras na matriz
    colocar_palavras_na_matriz(matriz, palavras, tamanho_linhas_matriz, tamanho_colunas_matriz)
    # preenchendo a matriz com letras aleatorias no lugar dos vazios
    matriz = preenchendo_matriz(matriz, tamanho_linhas_matriz, tamanho_colunas_matriz)
    # printando a matriz
    printar_matriz(matriz)
    # printando as palavras
    printar_palavras(palavras)

# chamando a função principal
if __name__ == "__main__":
    main()