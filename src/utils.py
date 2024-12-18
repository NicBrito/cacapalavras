# função para verificar se o usuário ainda possui tentativas
def verificar_tentativas_restantes(tentativas):
    if(tentativas == 0): # caso o usuário não tenha mais tentativas
        print("Você excedeu o número de tentativas!") # informando que o usuário excedeu o número de tentativas
        exit() # finalizando o programa
    return True # retornando que o usuário possui tentativas

# função para verificar se a posição dita pelo usuário é válida
def validar_posicao_usuario(posicao, tamanho_matriz):
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
def tratar_posicao_usuario(posicao):
    posicao = tuple(map(int, posicao.replace(' ', '').strip('()').split(','))) # transformando a posição em uma tupla
    return posicao # retornando a posição tratada