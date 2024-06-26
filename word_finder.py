'''
    Módulo para encontrar as palavras no caça-palavras.

    O módulo recebe a matriz do caça-palavras e as palavras que estão contidas nela. Nesse módulo, o usuário irá ditar a posição que acredita estar uma palavra
    e o módulo irá verificar se a palavra está contida na matriz na posição dita pelo usuário. Caso esteja, a palavra será marcada na matriz e o usuário poderá
    informar a próxima posição. Caso a palavra não esteja na posição dita pelo usuário, o módulo informará que a posição está incorreta e o usuário poderá tentar
    novamente. A cada erro do usuário será incrementado um contador de erros e o módulo informará quantos erros o usuário cometeu. O usuário poderá encerrar a
    procura de palavras a qualquer momento, informando nenhuma posição para a palavra. Caso desista de procurar as palavras, o módulo irá marcar todas as palavras
    escondidas na matriz e informar ao usuário quantos foram os seus erros. Caso o usuário encontre todas as palavras, o módulo informará quantos erros o usuário
    cometeu e o parabenizará por ter encontrado todas as palavras. As letras na matriz estão em maiúsculas e, quando uma palavra é marcada, as letras da palavra
    ficaram minúsculas.

    Parameters:
        - matriz (list): matriz do caça-palavras.
        - palavras (dic): dicionário com as palavras que estão contidas na matriz e suas posições.
'''

import cacapalavras
import os

# função para manter apenas as palavras marcadas na matriz
def manter_apenas_palavras_marcadas_na_matriz(matriz):
    for linha in range(0, len(matriz)): # percorrendo as linhas da matriz
        for coluna in range(0, len(matriz)): # percorrendo as colunas da matriz
            if not (matriz[linha][coluna] == matriz[linha][coluna].lower()): # verificando se a letra não está marcada
                matriz[linha][coluna] = " " # removendo letra não marcada
    return matriz # retornando a matriz com apenas as palavras marcadas

# função para encerrar a procura de palavras no caça-palavras
def encerramento(matriz, palavras, erros):
    os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
    matriz = manter_apenas_palavras_marcadas_na_matriz(matriz) # mantendo apenas as palavras marcadas na matriz
    cacapalavras.exibir_cacapalavras(matriz, palavras) # exibindo o caça-palavras
    print(f'Você cometeu {"nenhum" if(erros == 0) else "1"} erro!') if(0 <= erros <= 1) else print(f'Você cometeu {erros} erros!') # informando ao usuário quantos erros ele cometeu

# função para marcar a palavra no dicionário
def marcar_palavra_no_dicionario(palavras, palavra_na_matriz):
    dados_da_palavra = palavras[palavra_na_matriz] # obtendo os dados da palavra
    palavras[palavra_na_matriz.lower()] = dados_da_palavra # adicionando a palavra marcada no dicionário
    del palavras[palavra_na_matriz] # removendo a palavra não marcada do dicionário
    palavras = cacapalavras.reordenar_palavras(palavras, "alfabética") # reordenando as palavras no dicionário para a ordem alfabética
    return palavras # retornando o dicionário com a palavra marcada

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

# função para descobrir o tamanho entre duas posições na matriz
def descobrir_tamanho_palavra(posicao_inicial, posicao_final):
    tamanho = max(abs(posicao_final[0] - posicao_inicial[0]), abs(posicao_final[1] - posicao_inicial[1])) + 1 # descobrindo o tamanho da palavra
    return tamanho # retornando o tamanho da palavra

# função para descobrir a posição da palavra nas posições ditas pelo usuário
def descobrir_posicao(posicao_inicial, posicao_final):
    '''
        Função para descobrir a posição da palavra nas posições ditas pelo usuário.

        Parameters:
            - posição inicial (tuple): posição inicial da palavra no caça-palavras.
            - posição final (tuple): posição final da palavra no caça-palavras.

        Output:
            - posição (str): posição da palavra nas posições ditas pelo usuário.
    '''
    if(posicao_inicial[0] == posicao_final[0]): # verificando se a palavra está na horizontal
        if(posicao_inicial[1] < posicao_final[1]): # verificando se a palavra está da esquerda para a direita
            return 'horizontal' # retornando a posição da palavra
        else: # caso a palavra esteja da direita para a esquerda
            return 'horizontal invertida' # retornando a posição da palavra
    elif(posicao_inicial[1] == posicao_final[1]): # verificando se a palavra está na vertical
        if(posicao_inicial[0] < posicao_final[0]): # verificando se a palavra está de cima para baixo
            return 'vertical' # retornando a posição da palavra
        else: # caso a palavra esteja de baixo para cima
            return 'vertical invertida' # retornando a posição da palavra
    elif(posicao_inicial[0] < posicao_final[0]): # verificando se a palavra está na diagonal
        if(posicao_inicial[1] < posicao_final[1]): # verificando se a palavra está para direita
            return 'diagonal para direita' # retornando a posição da palavra
        else: # caso a palavra esteja para esquerda
            return 'diagonal para esquerda' # retornando a posição da palavra
    elif(posicao_inicial[0] > posicao_final[0]): # verificando se a palavra está na diagonal invertida
        if(posicao_inicial[1] > posicao_final[1]): # verificando se a palavra está para direita
            return 'diagonal para direita invertida' # retornando a posição da palavra
        else: # caso a palavra esteja para esquerda
            return 'diagonal para esquerda invertida' # retornando a posição da palavra
    return '' # caso a palavra não esteja em nenhuma posição válida, retornando que a posição é inválida

# função para obter a palavra existente na matriz na posição dita pelo usuário
def obter_palavra_existente_na_matriz(matriz, posicao_inicial, posicao_final):
    '''
        Função para obter a palavra existente na matriz na posição dita pelo usuário.

        Parameters:
            - matriz (list): matriz do caça-palavras.
            - posição inicial (tuple): posição inicial da palavra no caça-palavras.
            - posição final (tuple): posição final da palavra no caça-palavras.

        Output:
            - palavra na matriz (str): palavra existente na matriz na posição dita pelo usuário.
    '''
    tamanho_palavra = descobrir_tamanho_palavra(posicao_inicial, posicao_final) # descobrindo o tamanho da palavra
    posicao = descobrir_posicao(posicao_inicial, posicao_final) # descobrindo a posição da palavra
    invertida = False # marcando que a palavra não está invertida
    if("invertida" in posicao): # caso a posição seja invertida
        posicao = posicao.replace(" invertida", "") # removendo a palavra invertida da posição
        posicao_inicial, posicao_final = posicao_final, posicao_inicial # invertendo a posição inicial e final
        invertida = True # marcando que a palavra está invertida
    palavra_na_matriz = cacapalavras.obter_palavra_existente_na_matriz(matriz, posicao, tamanho_palavra, posicao_inicial[0] - 1, posicao_inicial[1] - 1) # obtendo a palavra existente na matriz
    if(invertida): # verificando se a palavra está invertida
        palavra_na_matriz = palavra_na_matriz[::-1] # invertendo a palavra
    return palavra_na_matriz # retornando a palavra existente na matriz

# função para verificar se a posição dita pelo usuário é válida
def validar_posicao(posicao, tamanho_matriz):
    try: # tentando separar a linha e a coluna da posição dita pelo usuário
        linha, coluna = map(int, posicao.strip('()').split(',')) # separando a linha e a coluna da posição
    except ValueError: # caso não seja possível separar a linha e a coluna da posição dita pelo usuário
        print('Posição inválida! Digite uma posição válida.') # informando ao usuário que a posição é inválida
        return False # retornando que a posição é inválida
    if not ((0 < linha <= tamanho_matriz + 1) and (0 < coluna <= tamanho_matriz + 1)): # verificando se a posição dita pelo usuário está dentro da matriz
        print('Posição inválida! Digite uma posição válida.') # informando ao usuário que a posição é inválida
        return False # retornando que a posição é inválida
    return True # retornando que a posição é válida

# função para tratar a posição dita pelo usuário
def tratar_posicao(posicao):
    posicao = tuple(map(int, posicao.replace(' ', '').strip('()').split(','))) # transformando a posição em uma tupla
    return posicao # retornando a posição tratada

# função para solicitar a posição da palavra ao usuário
def pedir_posicao(tamanho_matriz):
    '''
        Função para pedir a posição da palavra ao usuário.

        Parameters:
            - tamanho da matriz (int): tamanho da matriz do caça-palavras.

        Input:
            - posição (str): posição da palavra no caça-palavras.

        Output:
            - posição inicial (tuple): posição inicial da palavra no caça-palavras.
            - posição final (tuple): posição final da palavra no caça-palavras.
    '''
    tentativas = 3 # quantidade de tentativas para o usuário digitar uma posição válida
    print(f'\nPara finalizar a digitação, digite ENTER') # informando ao usuário como finalizar a procura de palavras
    for indice in range(0, 2): # pedindo as posições da palavra ao usuário
        while(cacapalavras.verificar_tentativas_restantes(tentativas)): # enquanto a posição for inválida
            posicao = input(f'Digite a posição {["inicial", "final"][indice]} da palavra (linha, coluna): ') # pedindo a posição da palavra
            if(cacapalavras.finalizar_coletar_palavras(posicao)): # verificando se o usuário deseja encerrar a procura de palavras
                return '', '' # encerrando a procura de palavras
            if(validar_posicao(posicao, tamanho_matriz)): # verificando se a posição dita pelo usuário é válida
                if(indice == 1 and tratar_posicao(posicao) == posicao_inicial): # verificando se a posição final é igual a posição inicial
                    print('Posição final não pode ser igual a posição inicial! Digite uma posição válida.') # informando ao usuário que a posição final não pode ser igual a posição inicial
                else: # caso a posição final não seja igual a posição inicial
                    break # não pedir nova posição
            tentativas -= 1 # decrementando a quantidade de tentativas, caso a posição seja inválida
        if(indice == 0): # verificando se é a posição inicial
            posicao_inicial = tratar_posicao(posicao) # criando a tupla da posição inicial
        else: # caso seja a posição final
            posicao_final = tratar_posicao(posicao) # criando a tupla da posição final
    return posicao_inicial, posicao_final # retornando a posição inicial e final

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
        cacapalavras.exibir_cacapalavras(matriz, palavras) # exibindo o caça-palavras
        posicao_inicial, posicao_final = pedir_posicao(len(matriz)) # pedindo a posição da palavra ao usuário
        if(not posicao_inicial or not posicao_final): # verificando se o usuário deseja encerrar a procura de palavras
            matriz = marcar_todas_palavras_na_matriz(matriz, palavras) # marcando todas as palavras na matriz
            encerramento(matriz, palavras, erros) # encerrando a procura de palavras
            print(f'Procura de palavras encerrada!') # informando ao usuário que a procura de palavras foi encerrada
            break # encerrando a procura de palavras
        palavra_na_matriz = "".join(obter_palavra_existente_na_matriz(matriz, posicao_inicial, posicao_final)).upper() # obtendo a palavra na matriz
        if(palavra_na_matriz in lista_palavras): # verificando se a palavra está na lista de palavras que devem ser encontradas
            matriz = marcar_palavra_na_matriz(matriz, posicao_inicial, posicao_final) # marcando a palavra na matriz
            palavras = marcar_palavra_no_dicionario(palavras, palavra_na_matriz) # marcando a palavra no dicionário
            acertos += 1 # incrementando a quantidade de acertos
        else: # caso a palavra não esteja na lista de palavras que devem ser encontradas
            erros += 1 # incrementando a quantidade de erros

# chamando a função principal
# if __name__ == '__main__':
#     matriz = [
#         ['B', 'O', 'L', 'A', 'O'],
#         ['B', 'G', 'H', 'T', 'J'],
#         ['L', 'O', 'S', 'N', 'O'],
#         ['T', 'U', 'N', 'E', 'L'],
#         ['S', 'V', 'Z', 'E', 'Y']
#              ] # matriz do caça-palavras
#     palavras = {'BOLA': {'posicao': {'inicial': (1,1), 'final': (1,4)}},
#                 'BONE': {'posicao': {'inicial': (2,1), 'final': (5,4)}},
#                 'LUZ': {'posicao': {'inicial': (3,1), 'final': (5,3)}},
#                 'TUNEL': {'posicao': {'inicial': (4,1), 'final': (4,5)}},
#                 'SUSTO': {'posicao': {'inicial': (5,1), 'final': (1,5)}}} # palavras do caça-palavras
#     main(matriz, palavras)