# função para contar posições permitidas
def sem_sobreposicao_contar_posicoes_vazias(matriz, linha, coluna, contador):
    if(matriz[linha][coluna] == ""): # caso a posição da matriz seja um vazio
        contador += 1 # incrementando o contador
    else: # caso a posição da matriz não seja um vazio
        contador = 0 # zerando o contador
    return contador # retornando o contador

# função de verificação das diagonais para esquerda
def sem_sobreposicao_verificar_diagonal_esquerda(matriz, tamanho_palavra, quantidade_linhas, linha, coluna):
    contador = 0 # criando contador
    while(linha < quantidade_linhas and coluna >= 0): # enquanto a linha for menor que o tamanho da matriz e a coluna for maior ou igual a zero
        contador = sem_sobreposicao_contar_posicoes_vazias(matriz, linha, coluna, contador) # chamando função para contar posições permitidas
        if(contador == tamanho_palavra): # caso o contador seja igual ao tamanho da palavra
            return True # retornando que a posição diagonal para a esquerda é permitida
        linha += 1 # incrementando a linha
        coluna -= 1 # incrementando a coluna
    return False # retornando que a posição diagonal para a esquerda não é permitida

# função para verificar se a posição diagonal para a esquerda é permitida
def sem_sobreposicao_verificar_posicao_diagonal_esquerda(matriz, tamanho_palavra, quantidade_colunas, quantidade_linhas):
    for coluna in range(tamanho_palavra - 1, quantidade_colunas - 1): # percorrendo cada coluna da matriz
        if(sem_sobreposicao_verificar_diagonal_esquerda(matriz, tamanho_palavra, quantidade_linhas, 0, coluna)): # verificar se a posição diagonal para a esquerda é permitida
            return True # retornando que a posição diagonal para a esquerda é permitida
    for linha in range(0, quantidade_linhas - tamanho_palavra + 1): # percorrendo cada linha da matriz
        if(sem_sobreposicao_verificar_diagonal_esquerda(matriz, tamanho_palavra, quantidade_linhas, linha, quantidade_colunas - 1)): # verificar se a posição diagonal para a esquerda é permitida
            return True # retornando que a posição diagonal para a esquerda é permitida
    return False # retornando que a posição diagonal para a esquerda não é permitida

# função de verificação das diagonais para direita
def sem_sobreposicao_verificar_diagonal_direita(matriz, tamanho_palavra, quantidade_colunas, quantidade_linhas, linha, coluna):
    contador = 0 # criando contador
    while(linha < quantidade_linhas and coluna < quantidade_colunas): # enquanto a linha e a coluna forem menores que o tamanho da matriz
        contador = sem_sobreposicao_contar_posicoes_vazias(matriz, linha, coluna, contador) # chamando função para contar posições permitidas
        if(contador == tamanho_palavra): # caso o contador seja igual ao tamanho da palavra
            return True # retornando que a posição diagonal para a direita é permitida
        linha += 1 # incrementando a linha
        coluna += 1 # incrementando a coluna
    return False # retornando que a posição diagonal para a direita não é permitida

# função para verificar se a posição diagonal para a direita é permitida
def sem_sobreposicao_verificar_posicao_diagonal_direita(matriz, tamanho_palavra, quantidade_colunas, quantidade_linhas):
    for coluna in range(0, quantidade_colunas - tamanho_palavra + 1): # percorrendo cada coluna da matriz
        if(sem_sobreposicao_verificar_diagonal_direita(matriz, tamanho_palavra, quantidade_colunas, quantidade_linhas, 0, coluna)): # verificar se a posição diagonal para a direita é permitida
            return True # retornando que a posição diagonal para a direita é permitida
    for linha in range(1, quantidade_linhas - tamanho_palavra + 1): # percorrendo cada linha da matriz
        if(sem_sobreposicao_verificar_diagonal_direita(matriz, tamanho_palavra, quantidade_colunas, quantidade_linhas, linha, 0)): # verificar se a posição diagonal para a direita é permitida
            return True # retornando que a posição diagonal para a direita é permitida
    return False # retornando que a posição diagonal para a direita não é permitida

# função para verificar se a posição vertical é permitida
def sem_sobreposicao_verificar_posicao_vertical(matriz, tamanho_palavra, quantidade_colunas, quantidade_linhas):
    for coluna in range(0, quantidade_colunas): # percorrendo cada coluna da matriz
        contador = 0 # criando contador
        for linha in range(0, quantidade_linhas): # percorrendo cada linha da coluna
            contador = sem_sobreposicao_contar_posicoes_vazias(matriz, linha, coluna, contador) # chamando função para contar posições permitidas
            if(contador == tamanho_palavra): # caso o contador seja igual ao tamanho da palavra
                return True # retornando que a posição vertical é permitida
    return False # retornando que a posição vertical não é permitida

# função para verificar se a posição horizontal é permitida
def sem_sobreposicao_verificar_posicao_horizontal(matriz, tamanho_palavra, quantidade_colunas, quantidade_linhas):
    for linha in range(0, quantidade_linhas): # percorrendo cada linha da matriz
        contador = 0 # criando contador
        for coluna in range(0, quantidade_colunas): # percorrendo cada coluna da linha
            contador = sem_sobreposicao_contar_posicoes_vazias(matriz, linha, coluna, contador) # chamando função para contar posições permitidas
            if(contador == tamanho_palavra): # caso o contador seja igual ao tamanho da palavra
                return True # retornando que a posição horizontal é permitida
    return False # retornando que a posição horizontal não é permitida

# verificando posições permitidas para a palavra sem sobreposição
def sem_sobreposicao_verificar_posicoes(matriz, tamanho_palavra, quantidade_colunas, quantidade_linhas):
    posicoes = [] # criando lista de posições
    if(sem_sobreposicao_verificar_posicao_horizontal(matriz, tamanho_palavra, quantidade_colunas, quantidade_linhas)): # verificar se a posição horizontal é permitida
        posicoes.extend(["horizontal", "horizontal invertida"]) # adicionando posição horizontal na lista de posições
    if(sem_sobreposicao_verificar_posicao_vertical(matriz, tamanho_palavra, quantidade_colunas, quantidade_linhas)): # verificar se a posição vertical é permitida
        posicoes.extend(["vertical", "vertical invertida"]) # adicionando posição vertical na lista de posições
    if(sem_sobreposicao_verificar_posicao_diagonal_direita(matriz, tamanho_palavra, quantidade_colunas, quantidade_linhas)): # verificar se a posição diagonal para a direita é permitida
        posicoes.extend(["diagonal para direita", "diagonal para direita invertida"]) # adicionando posição diagonal para a direita na lista de posições
    if(sem_sobreposicao_verificar_posicao_diagonal_esquerda(matriz, tamanho_palavra, quantidade_colunas, quantidade_linhas)): # verificar se a posição diagonal para a esquerda é permitida
        posicoes.extend(["diagonal para esquerda", "diagonal para esquerda invertida"]) # adicionando posição diagonal para a esquerda na lista de posições
    return posicoes # retornando lista de posições