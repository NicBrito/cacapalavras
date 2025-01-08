# função para verificar se o usuário ainda possui tentativas
def verificar_tentativas_restantes(tentativas):
    if(tentativas == 0): # caso o usuário não tenha mais tentativas
        print("Você excedeu o número de tentativas!") # informando que o usuário excedeu o número de tentativas
        exit() # finalizando o programa
    return True # retornando que o usuário possui tentativas

# função para transformar uma string em uma tupla
def transformar_string_em_tupla(string):
    return tuple(map(int, string.replace(' ', '').strip('()').split(','))) # transformando string em tupla e a retornando

# função para verificar se a posição dita pelo usuário está dentro dos limites da matriz
def validar_posicao_dentro_da_matriz(matriz, posicao):
    linha, coluna = transformar_string_em_tupla(posicao) # separando a linha e a coluna da posição dita pelo usuário
    quantidade_linhas, quantidade_colunas = len(matriz), len(matriz[0]) # armazenando a quantidade de linhas e colunas da matriz
    if not (1 <= linha <= quantidade_linhas and 1 <= coluna <= quantidade_colunas): # caso a posição dita pelo usuário não esteja dentro dos limites da matriz
        print('Posição inválida! Digite uma posição válida.')  # informando ao usuário que a posição é inválida
        return False # retornando que a posição é inválida
    return True # retornando que a posição é válida

# função para validar o formato da posição dita pelo usuário
def validar_formato_da_posicao(posicao):
    try: # tentando separar a linha e a coluna da posição dita pelo usuário
        linha, coluna = posicao.replace(' ', '').strip('()').split(',')  # separando a linha e a coluna da posição dita pelo usuário
    except ValueError: # caso não seja possível separar a linha e a coluna da posição dita pelo usuário
        print('Posição inválida! Digite uma posição válida.')
        return False # retornando que a posição é inválida
    if not (linha.isdigit() and coluna.isdigit()): # caso a linha e a coluna não sejam números
        print('Posição inválida! Digite uma posição válida.') # informando ao usuário que a posição é inválida
        return False # retornando que a posição é inválida
    return True # retornando que a posição é válida

# função para validar se a posição dita pelo usuário é válida
def validar_posicao_de_entrada(matriz, posicao):
    if not (validar_formato_da_posicao(posicao)): # verificando se o formato da posição é inválido
        return False # retornando que a posição é inválida
    if not (validar_posicao_dentro_da_matriz(matriz, posicao)): # verificando se a posição está fora dos limites da matriz
        return False # retornando que a posição é inválida
    return True # retornando que a posição é válida

# função para validar se as posições da palavra são válidas
def validar_posicoes_da_palavra(posicao_inicial, posicao_final):
    linha_inicial, coluna_inicial = posicao_inicial # separando a linha e a coluna da posição inicial
    linha_final, coluna_final = posicao_final # separando a linha e a coluna da posição final
    if not (linha_inicial == linha_final or coluna_inicial == coluna_final or abs(linha_inicial - linha_final) == abs(coluna_inicial - coluna_final)): # verificando se as posições da palavra são inválidas
        return False # retornando que as posições da palavra são inválidas
    return True # retornando que as posições da palavra são válidas