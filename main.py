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
    while(True): # caso precise digitar novo valor para o tamanho da matriz
        tamanho_matriz = input("Defina o tamanho da matriz quadrada: ") # definindo o tamanho da matriz
        if(tamanho_matriz.isdigit()): # caso o tamanho da matriz seja um número inteiro
            tamanho_matriz = int(tamanho_matriz) # convertendo o tamanho da matriz para um número inteiro
            tamanho_linhas_matriz = tamanho_matriz # definindo o tamanho das linhas da matriz
            tamanho_colunas_matriz = tamanho_matriz # definindo o tamanho das colunas da matriz
            return tamanho_matriz, tamanho_linhas_matriz, tamanho_colunas_matriz # retornando valores da matriz
        else: # caso o tamanho da matriz não seja um número inteiro
            print("O tamanho da matriz deve ser um número inteiro!") # informando que o tamanho da matriz deve ser um número inteiro

# verificando se a palavra já existe
def palavra_ja_existe(palavras, palavra_digitada):
    for palavra in palavras: # percorrendo lista de palavras
        if(palavra == palavra_digitada): # caso a palavra da lista seja igual a palavra digitada
            print("A palavra já existe!") # informando que a palavra já existe
            return True # retornando que a palavra já existe
    return False # retornando que a palavra não existe

# verificando se a palavra possui um tamanho permitido
def palavra_possui_tamanho_permitido(palavra_digitada, tamanho_matriz):
    if(len(palavra_digitada) <= tamanho_matriz): # caso o usuário digite uma palavra que possua um tamanho permitido
        return True # retornando que a palavra possui um tamanho permitido
    print("A palavra possui um tamanho não permitido!") # informando que a palavra possui um tamanho não permitido
    return False # retornando que a palavra possui um tamanho não permitido

# verificando se a palavra possui apenas letras
def palavra_possui_apenas_letras(palavra_digitada):
    if(palavra_digitada.isalpha()): # caso a palavra digitada possua apenas letras
        return True # retornando que a palavra possui apenas letras
    print("A palavra deve possuir apenas letras!") # informando que a palavra deve possuir apenas letras
    return False # retornando que a palavra não possui apenas letras

# verificando se a digitação de palavras deve ser finalizada
def finalizar_digitar_palavras(palavra_digitada):
    if(not palavra_digitada # caso o usuário não digite nada
       or palavra_digitada.replace(" ", "") == ""): # caso o usuário digite apenas espaços
        return True # retornando que a digitação de palavras deve ser finalizada
    return False # retornando que a digitação de palavras não deve ser finalizada

# criando lista de palavras
def criar_palavras(tamanho_matriz):
    print("Você deve digitar até", tamanho_matriz, "palavras com no máximo", tamanho_matriz, "letras!"
          "\nPara finalizar a digitação, digite ENTER") # informando a quantidade de palavras que o usuário deve digitar
    palavras = [] # criando lista de palavras vazia
    for indice_palavra in range(0, tamanho_matriz): # percorrendo a quantidade de palavras que o usuário deve digitar
        while(True): # caso deva digitar uma nova palavra
            palavra_digitada = str(input(f'Digite a {indice_palavra+1}a palavra: ')) # pegando a palavra digitada
            palavra_digitada = palavra_digitada.replace(" ", "") # removendo espaços da palavra digitada
            if(finalizar_digitar_palavras(palavra_digitada)): # caso o usuário não digite nada ou apenas espaços
                break # finalizando a digitação de palavras
            if(palavra_possui_tamanho_permitido(palavra_digitada, tamanho_matriz) # caso a palavra possua um tamanho permitido
               and not palavra_ja_existe(palavras, palavra_digitada) # caso a palavra não exista
               and palavra_possui_apenas_letras(palavra_digitada)): # caso a palavra possua apenas letras
                palavras.append(palavra_digitada) # adicionando palavra na lista de palavras
                break # finalizando a digitação de palavras
        if(finalizar_digitar_palavras(palavra_digitada)): # caso deva finalizar a digitação de palavras antes do máximo possível
            break # finalizando a digitação de palavras
    return palavras # retornando lista de palavras

# criando a matriz do tamanho definido e a preenchendo com vazios
def criar_matriz(tamanho_linhas_matriz, tamanho_colunas_matriz):
    matriz = [] # criando matriz vazia
    for numero_linha in range(0, tamanho_colunas_matriz): # percorrendo linha por linha da matriz
        linha = [] # criando linha vazia
        for numero_coluna in range(0, tamanho_linhas_matriz): # percorrendo coluna por coluna da matriz
            linha.append("") # adicionando um espaço na linha
        matriz.append(linha) # adicionando linha na matriz
    return matriz # retornando matriz

# preenchendo a matriz com letras aleatorias no lugar dos vazios
def preenchendo_matriz(matriz, tamanho_linhas_matriz, tamanho_colunas_matriz):
    for numero_linha in range(0, tamanho_colunas_matriz): # percorrendo linha por linha da matriz
        for numero_coluna in range(0, tamanho_linhas_matriz): # percorrendo coluna por coluna da matriz
            if(matriz[numero_linha][numero_coluna] == ""): # caso a posição da matriz seja um vazio
                letra_aleatoria = random.choice(letras) # escolhendo letra aleatoria
                matriz[numero_linha][numero_coluna] = letra_aleatoria # adicionando letra aleatoria na linha
    return matriz # retornando matriz

# função para colocar as palavras na matriz
def colocando_palavras_na_matriz(matriz, palavra, direcao, linha_palavra, coluna_palavra):
    if(direcao == "horizontal"):
        for letra in palavra:
            matriz[linha_palavra][coluna_palavra] = letra
            coluna_palavra += 1
    elif(direcao == "vertical"):
        for letra in palavra:
            matriz[linha_palavra][coluna_palavra] = letra
            linha_palavra += 1
    elif(direcao == "diagonal_para_direita"):
        for letra in palavra:
            matriz[linha_palavra][coluna_palavra] = letra
            linha_palavra += 1
            coluna_palavra += 1
    elif(direcao == "diagonal_para_esquerda"):
        for letra in palavra:
            matriz[linha_palavra][coluna_palavra] = letra
            linha_palavra += 1
            coluna_palavra -= 1

# função para checar sobreposição de palavras na matriz
def checar_sobreposicao_palavras(palavra_existente_na_matriz):
    if(palavra_existente_na_matriz == ""): # caso a palavra existente na matriz seja vazia
        return False # não vai sobrepor outra palavra
    else: # caso a palavra existente na matriz não seja vazia
        return True # vai sobrepor outra palavra

# função para pegar a palavra que já existe na matriz
def checar_palavra_existente_na_matriz(matriz, direcao, tamanho_palavra, linha_palavra, coluna_palavra):
    palavra_existente_na_posicao = "" # criando variável para armazenar a palavra que já existe na posição
    if(direcao == "horizontal"): # caso a direção seja horizontal
        for indice in range(0, tamanho_palavra): # percorrendo a quantidade de letras da palavra
            palavra_existente_na_posicao += matriz[linha_palavra][coluna_palavra] # adicionando a letra existente na variável
            coluna_palavra += 1 # selecionado próxima coluna para pegar a próxima letra da palavra
    elif(direcao == "vertical"): # caso a direção seja vertical
        for indice in range(0, tamanho_palavra): # percorrendo a quantidade de letras da palavra
            palavra_existente_na_posicao += matriz[linha_palavra][coluna_palavra] # adicionando a letra existente na variável
            linha_palavra += 1 # selecionado próxima linha para pegar a próxima letra da palavra
    elif(direcao == "diagonal_para_direita"): # caso a direção seja diagonal para a direita
        for indice in range(0, tamanho_palavra): # percorrendo a quantidade de letras da palavra
            palavra_existente_na_posicao += matriz[linha_palavra][coluna_palavra] # adicionando a letra existente na variável
            linha_palavra += 1 # selecionado próxima linha para pegar a próxima letra da palavra
            coluna_palavra += 1 # selecionado próxima coluna para pegar a próxima letra da palavra
    elif(direcao == "diagonal_para_esquerda"): # caso a direção seja diagonal para a esquerda
        for indice in range(0, tamanho_palavra): # percorrendo a quantidade de letras da palavra
            palavra_existente_na_posicao += matriz[linha_palavra][coluna_palavra] # adicionando a letra existente na variável
            linha_palavra += 1 # selecionado próxima linha para pegar a próxima letra da palavra
            coluna_palavra -= 1 # selecionado próxima coluna para pegar a próxima letra da palavra
    return palavra_existente_na_posicao # retornando a palavra que já existe na posição

# função para escolher posição aleatória para a palavra
def escolher_posicao_aleatoria_para_palavra(direcao, tamanho_linhas_matriz, tamanho_colunas_matriz, tamanho_palavra):
    if(direcao == "horizontal"):
        linha_palavra = random.randint(0, tamanho_colunas_matriz-1)
        coluna_palavra = random.randint(0, tamanho_linhas_matriz-tamanho_palavra)
    elif(direcao == "vertical"):
        linha_palavra = random.randint(0, tamanho_colunas_matriz-tamanho_palavra)
        coluna_palavra = random.randint(0, tamanho_linhas_matriz-1)
    elif(direcao == "diagonal_para_direita"):
        linha_palavra = random.randint(0, tamanho_colunas_matriz-tamanho_palavra)
        coluna_palavra = random.randint(0, tamanho_linhas_matriz-tamanho_palavra)
    elif(direcao == "diagonal_para_esquerda"):
        linha_palavra = random.randint(0, tamanho_colunas_matriz-tamanho_palavra)
        coluna_palavra = random.randint(tamanho_palavra-1, tamanho_linhas_matriz-1)
    else:
        linha_palavra = 0
        coluna_palavra = 0
    return linha_palavra, coluna_palavra # retornando a linha e a coluna da palavra

# função para colocar as palavras na posição escolhida
def colocar_palavras_na_posicao(matriz, palavra, direcao, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz):
    while(True): # caso deva escolher uma nova posição para a palavra
        linha_palavra, coluna_palavra = escolher_posicao_aleatoria_para_palavra(direcao, tamanho_linhas_matriz, tamanho_colunas_matriz, tamanho_palavra) # escolhendo posicao aleatoria para a palavra
        palavra_existente_na_matriz = checar_palavra_existente_na_matriz(matriz, direcao, tamanho_palavra, linha_palavra, coluna_palavra) # checar palavra que já existe nessa posição na matriz
        palavra_vai_sobrepor_outra = checar_sobreposicao_palavras(palavra_existente_na_matriz) # checar se a palavra vai sobrepor outra palavra
        if(palavra_vai_sobrepor_outra == False): # se a palavra não for sobrescrever outra, colocar na matriz
            colocando_palavras_na_matriz(matriz, palavra, direcao, linha_palavra, coluna_palavra) # colocando a palavra na matriz
            break # não permitir a escolha de uma nova posição para a palavra

# verificando posições permitidas para a palavra
def posicoes_permitidas_para_palavra(matriz, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz):
    posicoes = ["horizontal", "vertical", "diagonal para esquerda", "diagonal para direita"] # criando lista de posições
    return posicoes # retornando lista de posições

# colocando as palavras na matriz
def colocar_palavras_na_matriz(matriz, palavras, tamanho_linhas_matriz, tamanho_colunas_matriz):
    for palavra in palavras: # para cada palavra na lista de palavras
        tamanho_palavra = len(palavra) # tamanho da palavra
        direcao = random.choice(posicoes_permitidas_para_palavra(matriz, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz)) # escolhendo direção aleatória para a palavra
        colocar_palavras_na_posicao(matriz, palavra, direcao, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz) # chamar a função para colocar as palavras na posição escolhida
        printar_matriz(matriz) # printando a matriz

# função principal
def main():
    tamanho_matriz, tamanho_linhas_matriz, tamanho_colunas_matriz = definir_tamanho_matriz() # definindo o tamanho da matriz
    matriz = criar_matriz(tamanho_linhas_matriz, tamanho_colunas_matriz) # criando a matriz do tamanho definido e a preenchendo com vazios
    palavras = criar_palavras(tamanho_matriz) # criando as palavras
    palavras_do_maior_pro_menor = palavras.sort(key=len, reverse=True) # reordenando as palavras para que as maiores fiquem primeiro
    colocar_palavras_na_matriz(matriz, palavras_do_maior_pro_menor, tamanho_linhas_matriz, tamanho_colunas_matriz) # colocando as palavras na matriz
    matriz = preenchendo_matriz(matriz, tamanho_linhas_matriz, tamanho_colunas_matriz) # preenchendo a matriz com letras aleatorias no lugar dos vazios
    printar_matriz(matriz) # printando a matriz
    palavras_em_ordem_alfabetica = palavras.sort() # reordenando as palavras para a ordem alfabética
    printar_palavras(palavras_em_ordem_alfabetica) # printando as palavras

# chamando a função principal
if __name__ == "__main__":
    main()