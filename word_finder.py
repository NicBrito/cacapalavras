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
            if (validar_posicao(posicao, tamanho_matriz)): # verificando se a posição dita pelo usuário é válida
                break # não pedir nova posição
            else: # caso a posição dita pelo usuário seja inválida
                tentativas -= 1 # decrementando a quantidade de tentativas
        if(indice == 0): # verificando se é a posição inicial
            posicao_inicial = tratar_posicao(posicao) # criando a tupla da posição inicial
        else: # caso seja a posição final
            posicao_final = tratar_posicao(posicao) # criando a tupla da posição final
    return posicao_inicial, posicao_final # retornando a posição inicial e final

# função principal
def main(matriz, palavras):
    for palavra in palavras:
        print(f'PALAVRA: {palavra.ljust(10)}\t\tPOSIÇÃO: {palavras[palavra]['posicao']['inicial']}{palavras[palavra]['posicao']['final']}')
    while(True): # procurando as palavras na matriz
        cacapalavras.exibir_matriz(matriz) # printando a matriz
        posicao_inicial, posicao_final = pedir_posicao(len(matriz)) # pedindo a posição da palavra ao usuário
        if(not posicao_inicial or not posicao_final): # verificando se o usuário deseja encerrar a procura de palavras
            print(f'Procura de palavras encerrada!') # informando ao usuário que a procura de palavras foi encerrada
            break # encerrando a procura de palavras
        palavra_na_matriz = "".join(obter_palavra_existente_na_matriz(matriz, posicao_inicial, posicao_final)) # obtendo a palavra na matriz
        if(palavra_na_matriz in list(palavras.keys())): # verificando se a palavra está na lista de palavras que devem ser encontradas
            print(f'Palavra {palavra_na_matriz} encontrada!') # informando ao usuário que a palavra foi encontrada
        else: # caso a palavra não esteja na lista de palavras que devem ser encontradas
            print(f'Palavra não encontrada! Palavra na matriz foi {palavra_na_matriz.upper()}') # informando ao usuário que a palavra não foi encontrada

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