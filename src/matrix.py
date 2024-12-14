import random
from constants import LETRAS
from words import descobrir_tamanho_palavra, descobrir_posicao

# criando a matriz do tamanho definido e a preenchendo com vazios
def gerar_matriz_vazia(tamanho_linhas_matriz, tamanho_colunas_matriz):
    matriz = [] # criando matriz vazia
    for linha in range(0, tamanho_colunas_matriz): # percorrendo linha por linha da matriz
        linha_vazia = [] # criando linha vazia
        for coluna in range(0, tamanho_linhas_matriz): # percorrendo coluna por coluna da matriz
            linha_vazia.append("") # adicionando um espaço vazio na linha
        matriz.append(linha_vazia) # adicionando linha na matriz
    return matriz # retornando matriz

# preenchendo a matriz com letras aleatorias no lugar dos vazios
def preencher_matriz_com_letras_aleatorias(matriz, tamanho_linhas_matriz, tamanho_colunas_matriz):
    for linha in range(0, tamanho_colunas_matriz): # percorrendo linha por linha da matriz
        for coluna in range(0, tamanho_linhas_matriz): # percorrendo coluna por coluna da matriz
            if(matriz[linha][coluna] == ""): # caso a posição da matriz seja um vazio
                letra_aleatoria = random.choice(LETRAS) # escolhendo letra aleatoria
                matriz[linha][coluna] = letra_aleatoria.upper() # adicionando letra aleatoria na linha
    return matriz # retornando matriz

# função para manter apenas as palavras marcadas na matriz
def manter_apenas_palavras_marcadas_na_matriz(matriz):
    for linha in range(0, len(matriz)): # percorrendo as linhas da matriz
        for coluna in range(0, len(matriz)): # percorrendo as colunas da matriz
            if not (matriz[linha][coluna] == matriz[linha][coluna].lower()): # verificando se a letra não está marcada
                matriz[linha][coluna] = " " # removendo letra não marcada
    return matriz # retornando a matriz com apenas as palavras marcadas

# função para marcar a palavra na matriz
def marcar_palavra_na_matriz(matriz, posicao_inicial, posicao_final):
    tamanho_palavra = descobrir_tamanho_palavra(posicao_inicial, posicao_final) # descobrindo o tamanho da palavra
    posicao = descobrir_posicao(posicao_inicial, posicao_final) # descobrindo a posição da palavra
    if("invertida" in posicao): # verificando se a posição é invertida
        posicao = posicao.replace(" invertida", "") # removendo a palavra invertida da posição
        posicao_inicial, posicao_final = posicao_final, posicao_inicial # invertendo a posição inicial e final
    linha_palavra, coluna_palavra = posicao_inicial[0] - 1, posicao_inicial[1] - 1 # criando variáveis para a linha e a coluna da palavra
    for indice in range(0, tamanho_palavra): # percorrendo a quantidade de letras da palavra
        matriz[linha_palavra][coluna_palavra] = matriz[linha_palavra][coluna_palavra].lower() # marcando a letra da palavra na matriz
        match posicao: # verificando a posição da palavra
            case "horizontal": # caso a posição seja horizontal
                coluna_palavra += 1 # selecionado próxima coluna
            case "vertical": # caso a posição seja vertical
                linha_palavra += 1 # selecionado próxima linha
            case "diagonal para direita": # caso a posição seja diagonal para a direita
                linha_palavra += 1 # selecionado próxima linha
                coluna_palavra += 1 # selecionado próxima coluna
            case "diagonal para esquerda": # caso a posição seja diagonal para a esquerda
                linha_palavra += 1 # selecionado próxima linha
                coluna_palavra -= 1 # selecionado próxima coluna
    return matriz # retornando a matriz com a palavra marcada

# função para marcar todas as palavras na matriz
def marcar_todas_palavras_na_matriz(matriz, palavras):
    lista_palavras = list(palavras.keys()) # criando uma lista com as palavras que devem ser encontradas
    for palavra in lista_palavras: # percorrendo as palavras do dicionário
        posicao_inicial = palavras[palavra]['posicao']['inicial'] # obtendo a posição inicial da palavra
        posicao_final = palavras[palavra]['posicao']['final'] # obtendo a posição final da palavra
        matriz = marcar_palavra_na_matriz(matriz, posicao_inicial, posicao_final) # marcando a palavra na matriz
    return matriz # retornando a matriz com todas as palavras marcadas