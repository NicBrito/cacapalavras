import os
from display import exibir_cacapalavras
from input_handlers import buscador_solicitar_posicao
from matrix import matriz_marcar_palavra, matriz_marcar_todas_palavras, matriz_manter_apenas_palavras_marcadas
from core import obter_palavra_existente_na_matriz
from words import palavras_marcar_no_dicionario, palavras_descobrir_tamanho, palavras_descobrir_posicao

# função para obter a palavra existente na matriz na posição dita pelo usuário
def obter_palavra_existente_na_matriz_na_posicao(matriz, posicao_inicial, posicao_final):
    tamanho_palavra = palavras_descobrir_tamanho(posicao_inicial, posicao_final) # descobrindo o tamanho da palavra
    posicao = palavras_descobrir_posicao(posicao_inicial, posicao_final) # descobrindo a posição da palavra
    invertida = False # marcando que a palavra não está invertida
    if("invertida" in posicao): # caso a posição seja invertida
        posicao = posicao.replace(" invertida", "") # removendo a palavra invertida da posição
        posicao_inicial, posicao_final = posicao_final, posicao_inicial # invertendo a posição inicial e final
        invertida = True # marcando que a palavra está invertida
    palavra_na_matriz = obter_palavra_existente_na_matriz(matriz, posicao, tamanho_palavra, posicao_inicial[0] - 1, posicao_inicial[1] - 1) # obtendo a palavra existente na matriz
    if(invertida): # verificando se a palavra está invertida
        palavra_na_matriz = palavra_na_matriz[::-1] # invertendo a palavra
    return palavra_na_matriz # retornando a palavra existente na matriz

# função para encerrar a procura de palavras no caça-palavras
def encerramento(matriz, palavras, erros):
    os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
    matriz = matriz_manter_apenas_palavras_marcadas(matriz) # mantendo apenas as palavras marcadas na matriz
    exibir_cacapalavras(matriz, palavras) # exibindo o caça-palavras
    print(f'Você cometeu {"nenhum" if(erros == 0) else "1"} erro!') if(0 <= erros <= 1) else print(f'Você cometeu {erros} erros!') # informando ao usuário quantos erros ele cometeu

# função principal
def main(matriz, palavras):
    acertos = 0 # quantidade de acertos do usuário
    erros = 0 # quantidade de erros do usuário
    lista_palavras = list(palavras.keys()) # criando uma lista com as palavras que devem ser encontradas
    while(True): # procurando as palavras na matriz
        if(acertos == len(lista_palavras)): # verificando se o usuário encontrou todas as palavras
            encerramento(matriz, palavras, erros) # encerrando a procura de palavras
            print(f'Parabéns! Você encontrou todas as palavras!') # informando ao usuário que ele encontrou todas as palavras
            break # encerrando a procura de palavras
        os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
        exibir_cacapalavras(matriz, palavras) # exibindo o caça-palavras
        posicao_inicial, posicao_final = buscador_solicitar_posicao(len(matriz)) # pedindo a posição da palavra ao usuário
        if(not posicao_inicial or not posicao_final): # verificando se o usuário deseja encerrar a procura de palavras
            matriz = matriz_marcar_todas_palavras(matriz, palavras) # marcando todas as palavras na matriz
            encerramento(matriz, palavras, erros) # encerrando a procura de palavras
            print(f'Procura de palavras encerrada!') # informando ao usuário que a procura de palavras foi encerrada
            break # encerrando a procura de palavras
        palavra_na_matriz = "".join(obter_palavra_existente_na_matriz_na_posicao(matriz, posicao_inicial, posicao_final)).upper() # obtendo a palavra na matriz
        if(palavra_na_matriz in lista_palavras): # verificando se a palavra está na lista de palavras que devem ser encontradas
            matriz = matriz_marcar_palavra(matriz, posicao_inicial, posicao_final) # marcando a palavra na matriz
            palavras = palavras_marcar_no_dicionario(palavras, palavra_na_matriz) # marcando a palavra no dicionário
            acertos += 1 # incrementando a quantidade de acertos
        else: # caso a palavra não esteja na lista de palavras que devem ser encontradas
            erros += 1 # incrementando a quantidade de erros